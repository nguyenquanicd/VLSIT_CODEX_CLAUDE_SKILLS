# CAN RTL Design Analysis

## 1. Scope and evidence

This report accompanies `rtl_hierarchy.drawio`. The analysis is based on the supplied RTL directory, its `verilog` subdirectory, `verilog/README.txt`, and the nearby `syn/synplicity/can.prj`. Source references below are relative to the supplied RTL directory. No RTL source file was modified.

- Selected top: **can_top**, explicitly selected by `set_option -top_module` in the synthesis project.
- Source inventory: 13 Verilog files, including one definitions header; 12 module definitions.
- Active hierarchy: **57 module instances including TOP**, comprising 3 instances at depth 1 and 53 at depth 2 (35 register cells and 18 protocol helpers). Eleven module types are reachable; `can_register_syn` is defined but not instantiated.
- Configuration assumption: use the delivered `can_defines.v` with no additional command-line macro definitions. `CAN_WISHBONE_IF`, vendor RAM selections, and `CAN_BIST` are commented out. The drawing therefore represents the **8051-style host interface and behavioral receive memory**. External build definitions can change this hierarchy; they were not supplied.
- Runtime reset defaults: basic register mode (`extended_mode = 0`), controller reset mode asserted (`reset_mode = 1`), clock-divider control reset to zero, and error-warning limit 96. Some write-only storage cells do not have reset ports and require software initialization.
- Evidence level: static RTL analysis. No HDL compilation, simulation, synthesis, CDC analysis, formal proof, or standards conformance test was performed. Historical verification claims in `verilog/README.txt` are author statements, not results of this analysis.

## 2. Diagram interpretation

Tabs appear left to right as `00_TOP`, `01_LEVEL_1`, `02_LEVEL_2`. The final tab contains both depth-1 parent contexts and every active depth-2 instance; each repeated instance remains a separate block. Depth-1 `i_can_btl` is a leaf and does not repeat at depth 2.

Module labels contain exactly two lines: `instance_name`, then `(module_name)`. TOP uses `TOP` and `(can_top)`. Text is 18 pt; fills are white and outlines/text are black. Thin solid arrows mean instantiation. Thick dashed arrows mean functional relationships. Shared hierarchy trunks are drawing conventions, not hardware buses. External annotation arrows indicate interface associations; actual signal directions are stated in the annotations and tables below.

Detailed explanations are outside the block layout, in separate bordered note panels and this Markdown report. The diagram shows principal functional paths; it is not an exhaustive netlist or a cycle-accurate timing diagram. The two CRC helper links show the actual `calculated_crc` slices feeding their bit-order converters. No direct filter-to-FIFO connection is drawn: the filter's `id_ok` is consumed by parent BSP control before that parent generates FIFO writes.

## 3. Functions and supported features

| Function / feature | RTL implementation and evidence | Qualification |
|---|---|---|
| Host programming and readback | `can_top` address latch, host-edge strobes, register/FIFO read selection; `can_registers` address decode | 8-bit data and address; active-high `rd_i` / `wr_i`; default interface is multiplexed 8051 style |
| Optional Wishbone host | `can_top.v` conditional `CAN_WISHBONE_IF` branch, CYC/STB synchronization and ACK pulse generation | Alternative compile configuration; not active in this diagram; no protocol conformance result |
| CAN standard and extended frame parsing | `can_bsp.v:699-1056` frame phases through ID1, IDE, ID2, RTR, DLC, data, CRC, ACK and EOF | 11-bit and 29-bit ID paths are present; extended register mode is distinct from extended frame format |
| Payload and remote frames | `remote_rq`, `limited_data_len`, header packing and TX-chain assembly in `can_bsp.v:735-736, 1328-1407, 1693-1744` | Payload limited to 8 bytes; remote frames retain header information without received payload |
| Bit timing | `can_btl.v:257-475` prescaler, segments, phase correction, sampling and TX point | Programmable BRP/SJW/TSEG1/TSEG2 and optional majority triple sampling |
| Serialization and bit stuffing | `can_bsp.v:1074-1130, 1598-1762` TX selection, stuffing counters and TX pointers | Combinational bit-order helper instances support packed serial chains |
| CRC | `can_crc.v` recurrence and `can_bsp.v:1260-1267` | 15-bit accumulator; feedback polynomial constant `15'h4599`; initialized explicitly at frame start |
| Acceptance filtering | `can_acf.v` comparison masks and `id_ok` state; mapping at `can_bsp.v:1275-1321` | Basic matching and extended-mode single/dual filters; mask bit 1 means ignore that comparison |
| RX buffering | `can_fifo.v` data array, length metadata, overrun metadata, pointer/counter logic | 64-byte data capacity; 64 metadata slots do not imply capacity for 64 full frames |
| Error handling and arbitration | `can_bsp.v:738-750, 1890-2142` error conditions, arbitration capture, counters and bus-off state | Bit/stuff/form/ACK/CRC errors, error-active/passive transitions and recovery logic are present; unverified |
| Listen-only, self-test and self reception | Register-mode controls and BSP qualification of TX, ACK and self-frame storage | Extended-mode controls; normal receive processing remains distinct from these modes |
| Abort and single-shot TX | `can_registers.v:598-610`; BSP `need_to_tx` termination logic at `1765-1773` | Command semantics depend on command combinations and sample-point timing |
| Interrupts | `can_registers.v:1146-1256` cause latches, enables and `irq_n` | Active-low external `irq_on`; individual causes have different clear conditions |
| Programmable clock output | `can_registers.v:782-851` | Divider, clock bypass and clock-off selection; clock-off drives constant high |
| Software overload requests | `can_registers.v:615-635` | **Not supported**: instance is commented out and `overload_request` is tied to zero; automatic overload handling is a separate BSP path |
| CAN FD / AXI / APB | No corresponding port sets, longer payload datapath, or FD phase logic found in the analyzed RTL | Do not label this design as supporting these interfaces or CAN FD |

## 4. External interfaces

| Interface | Input signals | Output / bidirectional signals | Behavior |
|---|---|---|---|
| Default multiplexed host | `ale_i`, `rd_i`, `wr_i`, `cs_can_i` | `port_0_io[7:0]` bidirectional | Address captured on `clk_i` when ALE is high. A rising read/write strobe generates internal `cs` when selected. `port_0_io` drives registered read data while selected and reading; otherwise high impedance. No ready/acknowledge output exists in this branch. |
| Core clock and reset | `clk_i`, `rst_i` | — | Core processing is in `clk_i` domain; reset is active high. Many control registers use asynchronous assertion. |
| CAN pins | `rx_i` | `tx_o` | RX passes through two sequential synchronizer stages in TOP before BTL sampling. TX comes from BSP. These are digital transceiver-side signals, not a differential CAN physical layer. |
| Interrupt | — | `irq_on` | Connected to register bank `irq_n`; asserted low. |
| Bus-off indication | — | `bus_off_on` | BSP assigns `~node_bus_off`; asserted low despite the `_on` name. |
| Clock output | — | `clkout_o` | Connected to register bank programmable clock output. |
| Optional Wishbone | `wb_clk_i`, `wb_rst_i`, `wb_dat_i[7:0]`, `wb_cyc_i`, `wb_stb_i`, `wb_we_i`, `wb_adr_i[7:0]` | `wb_dat_o[7:0]`, `wb_ack_o` | Conditional alternative to the multiplexed host; synchronized transaction request and returned ACK pulse. No `SEL`, `ERR`, or `RTY` ports are present. |
| Optional BIST | `mbist_si_i`, `mbist_ctrl_i` | `mbist_so_o` | Requires CAN_BIST, its control-width definition, and appropriate memory implementation; inactive here. |

Primary port and integration evidence: `can_top.v:214-301, 443-737, 743-869`. TOP's 8051 host input strobes require adequate timing relative to `clk_i`; the RTL does not provide a transaction-completion handshake on that interface.

## 5. Principal internal functional relationships

| Source → destination | Key mapped signals | Functional meaning |
|---|---|---|
| TOP host logic → registers | `cs`, `we`, `addr[7:0]`, `data_in[7:0]` | Register reads/writes qualified by host access |
| Registers → TOP | `data_out_regs`, `irq_n`, `clkout` | Read-data response, interrupt and exported clock |
| Registers → BTL | `baud_r_presc[5:0]`, `sync_jump_width[1:0]`, `time_segment1[3:0]`, `time_segment2[2:0]`, `triple_sampling` | Timing configuration |
| BTL → BSP and selected register logic | `sample_point`, `sampled_bit`, `sampled_bit_q`, `tx_point`, `hard_sync` | Bit sampling and TX scheduling; `sample_point` also qualifies command handling in registers |
| BSP → BTL | `rx_idle`, `rx_inter`, `transmitting`, `transmitter`, `go_rx_inter`, `tx_next`, `go_overload_frame`, `go_error_frame`, `go_tx`, `send_ack`, `node_error_passive` | Protocol-state feedback for synchronization and bit timing |
| Registers → BSP | Modes, `tx_data_0..12`, acceptance codes/masks, `release_buffer`, `tx_request`, `abort_tx`, `self_rx_request`, `single_shot_transmission`, warning limit and counter-write strobes | Software-selected behavior, TX contents, filtering and receive-buffer management |
| BSP → registers | `tx_state`, `tx_state_q`, `node_bus_off`, `error_status`, error counters, TX/RX status, `tx_successful`, `need_to_tx`, FIFO status, IRQ event strobes and capture values | Status, error reporting and command completion context |
| TOP → BSP → FIFO | Host `addr`, FIFO selection, and FIFO read result through BSP `data_out` | Memory-mapped RX readback; TOP selects register or FIFO output |
| BSP → CRC | `sampled_bit`; enable = `crc_enable & sample_point & ~bit_de_stuff`; initialize = `go_crc_enable` | Accumulate unstuffed frame bits |
| CRC → BSP and CRC IBO helpers | `calculated_crc[14:0]` | RX CRC comparison and TX CRC packing |
| BSP → ACF → BSP | ID, mode, codes/masks, first payload bytes, RTR/IDE and frame phase; `id_ok` result | Acceptance decision; BSP qualifies FIFO commit with this result |
| BSP → FIFO → BSP | `wr_fifo`, `data_for_fifo[7:0]`, address, mode, release/select controls; `data_out`, `overrun`, `info_empty`, `info_cnt` | Frame-byte storage, host readout and occupancy/error status |
| BSP TX byte inputs → IBO → BSP TX chains | `tx_data_N` → `r_tx_data_N`, N = 0..12 | Pure combinational reversal of each 8-bit vector, not a handshake or FIFO |

The CRC IBO inputs are specifically `calculated_crc[14:7]` and `{calculated_crc[6:0], 1'b0}`. They produce `r_calculated_crc[7:0]` and `[15:8]`. Acceptance filter output is not a ready/valid interface. FIFO uses a write strobe and a release-buffer command; message metadata is committed when the write burst ends (`~wr & wr_q`).

## 6. Configuration and status registers

Addresses below are **decimal byte addresses**, not word offsets. Decode and read selection: `can_registers.v:444-485, 1084-1140`; FIFO window selection: `can_top.v:743-761`. Basic/extended mode and controller reset/operation mode alter the address meanings.

| Address | Basic mode | Extended mode | Access / condition |
|---|---|---|---|
| 0 | Reset bit and basic IRQ enables | Reset, listen-only, self-test, filter selection | Mode control; extended mode fields write only while controller reset mode is set |
| 1 | Command; reads `0xff` | Command; reads zero | TX request, abort/single-shot, RX release, clear-overrun and self-reception controls; command cells self-clear according to their RTL |
| 2 | Status | Status | Read-only live/latched status |
| 3 | Basic IRQ causes plus fixed upper bits | Extended IRQ causes | Reading clears selected causes; RX cause clears through buffer release/reset, not merely this register read |
| 4 | Acceptance code 0 in reset; otherwise read `0xff` | IRQ enable | Basic filter write requires reset mode; extended enable byte has no hardware reset |
| 5 | Acceptance mask 0 in reset; otherwise read `0xff` | No decoded register | Basic filter write requires reset mode |
| 6, 7 | Bus timing 0, 1 | Bus timing 0, 1 | Writable only in controller reset mode; storage has no hardware reset |
| 10..19 | TX header/data registers in operation | See individual entries below | Basic TX writes require available transmit buffer; basic RX reads use a different window |
| 11 | TX byte 1 when operating | Arbitration-lost capture | Extended capture read unlocks further capture |
| 12 | TX byte 2 when operating | Error-code capture | Extended capture read clears the code and unlocks capture |
| 13 | TX byte 3 when operating | Error-warning limit | Extended warning-limit writes require reset mode; reset value 96 |
| 14, 15 | TX bytes 4, 5 when operating | RX / TX error counters | Extended software counter writes require reset mode; internal counters are 9 bits, host sees low 8 bits |
| 16..19 | TX bytes 6..9 when operating | Acceptance codes 0..3 in reset; TX bytes 0..3 for writes in operation | Extended operating-mode reads select RX FIFO, not TX storage |
| 20..23 | RX read window | Acceptance masks 0..3 in reset; TX bytes 4..7 for writes in operation | Extended operating-mode reads select RX FIFO |
| 24..28 | RX read window | TX bytes 8..12 for writes in operation | Extended operating-mode reads select RX FIFO; reset-mode readback of these slots is zero |
| 29 | RX read window | RX message count | Extended count = `{1'b0, rx_message_counter}` |
| 31 | Clock divider / mode control | Clock divider / mode control | Bit 7 chooses extended register mode; bit 3 disables clock output; bits 2:0 select divider/bypass. High fields require reset mode for writes. |

Basic RX window: 20..29. Extended RX window: 16..28 while not in controller reset mode. Address windows overlap TX/filter storage intentionally; read/write direction and mode select the function. Acceptance storage and TX bytes use non-reset `can_register` cells.

### Status byte at address 2

| Bit | RTL field | Meaning |
|---|---|---|
| 7 | `node_bus_off` | Bus-off status |
| 6 | `error_status` | Warning threshold reached |
| 5 | `transmit_status` | Transmitting / relevant extended waiting state |
| 4 | `receive_status` | Receive / relevant extended waiting state |
| 3 | `transmission_complete` | TX success or abort recorded |
| 2 | `transmit_buffer_status` | Transmit buffer available |
| 1 | `overrun_status` | Latched receive overrun |
| 0 | `receive_buffer_status` | Receive message available |

### Extended IRQ byte at address 3

Bits 7..0 are bus error, arbitration lost, error passive, fixed zero, data overrun, error warning, transmit and receive. Basic mode exposes the low four causes with fixed high bits. Enables map to the corresponding extended byte bits, with bit 4 unused. Interrupt cause latches, their clear priorities, and external IRQ deassertion are separate logic: reading the IRQ register or releasing a buffer drives `irq_n` high; a remaining cause can reassert it later. Evidence: `can_registers.v:1146-1256`.

## 7. Implementation status, advantages and disadvantages

**Implemented in source:** classic CAN framing paths, programmable bit timing, masking filters, TX register storage, receive buffering, error confinement, status and interrupts. These statements describe code presence and traced behavior; they do not establish verification pass status.

**Advantages:** clear division between register, timing and protocol modules; selectable host interface; source-available behavioral receive storage; programmable filters and timing; error/status observability; reusable small register and bit-reversal helper modules.

**Limitations:** fixed classic CAN payload size; finite 64-byte receive storage; software initialization of several non-reset registers; legacy explicit sensitivity lists, implicit nets and simulation delays; asynchronous host integration needs timing/CDC review; vendor memories and BIST require separately available dependencies. BSP combines many protocol responsibilities in one large module, which complicates independent review. Software-triggered overload requests are disabled. Throughput, timing closure, area, power and protocol compliance were not measured.

The adjacent historical synthesis project selects `can_top` and lists external Actel memory files, but the delivered definitions do not enable the Actel RAM branch. It documents a possible integration target rather than proving that the active snapshot uses those RAM instances.

## 8. Potential bugs and review points

These findings are separated from confirmed feature limitations. Reproduction or a specification comparison is required before changing RTL.

| ID | Observation and source evidence | Potential impact / proposed check | Confidence and scope |
|---|---|---|---|
| CAN-R01 | `can_fifo.v:278-284, 341-358` advances `rd_info_pointer` on `release_buffer & ~info_full`, while `info_cnt` decrements on release only when `~info_empty`. | At metadata-full occupancy, release can decrement count without advancing its pointer; an empty release can advance the pointer without decrementing count. Review whether release should be qualified by nonempty metadata. Exercise metadata full, empty release, and simultaneous write/release. | High confidence in static mismatch; reachability of 64 metadata slots and permitted host behavior are unverified. |
| CAN-R02 | `can_registers.v:444-485, 1093-1140` read mux decodes `addr[4:0]`, but write and capture-read strobes compare full 8-bit addresses. | Addresses above 31 can alias read values without the corresponding write or read-to-clear effects. Determine whether system-level address qualification guarantees addresses 0..31. | Observed asymmetry; may be intentional if the host supplies a constrained address range. |
| CAN-R03 | At `can_top.v:787-831`, optional Wishbone request is synchronized, but `wb_we_i`, `wb_adr_i`, and `wb_dat_i` feed the core directly; `cs_ack1/2/3` and `wb_ack_o` have no explicit reset assignments. | Review the bundled-data stability assumption, reset/startup ACK behavior, clock ratios and back-to-back transfers. Add CDC/timing constraints only after confirming the intended integration contract. | Conditional risk; Wishbone branch is inactive in this drawing. No CDC or bus compliance result. |
| CAN-R04 | At `can_registers.v:715-1076`, `IRQ_EN_REG`, bus timing, acceptance and TX storage use `can_register`, which has no reset. | Uninitialized enables/timing/masks can propagate unknown values in simulation or unspecified startup behavior until software initializes them. Document mandatory initialization before leaving reset/entering extended mode. | Confirmed lack of reset; not automatically a bug if the software contract requires initialization. |
| CAN-R05 | At `can_top.v:837-869`, in the active host branch, ALE/read/write inputs are sampled without a transaction ACK. | Short or asynchronous strobes can be missed; read data is registered on a core clock, so the host must meet access timing. Confirm external timing constraints and sample pulse lengths. | Integration risk; no supplied timing contract was analyzed. |
| CAN-R06 | At `can_top.v:589, 666`, TOP uses `rx_inter` in child mappings without an explicit net declaration; legacy implicit-wire behavior supplies it. | A build using `default_nettype none` may reject the source; inspect strict compilation settings and declare the net if a portability update is authorized. | Static portability finding; no strict compilation was run. |
| CAN-R07 | At `can_fifo.v:369-376, 684-698`, FIFO metadata initialization runs over multiple clocks using `initialize_memories`; software may write/release during this period unless externally prevented. | Check reset-to-operation sequencing, initialization completion and any race with metadata writes. | Review hypothesis; no assertion or simulation trace confirms a failure. |

Known limitation separate from potential bugs: `overload_request` is assigned zero in `can_registers.v:635`. This does not remove the separate automatic overload-frame logic in BSP.

## 9. Complete active instance inventory

Parameters listed below are instance overrides as written in RTL, or `default` when absent. Standard top and protocol-module default `Tp` is 1; register helper defaults are defined in their corresponding module files. There are no active generate scopes in this snapshot. Commented-out `COMMAND_REG_OVERLOAD` is excluded.

| Depth | Instance path | Module | Instance parameters | Source |
|---|---|---|---|---|
| 0 | TOP | can_top | Tp = 1 (default) | verilog/can_top.v |
| 1 | TOP.i_can_registers | can_registers | default | verilog/can_top.v |
| 1 | TOP.i_can_btl | can_btl | default | verilog/can_top.v |
| 1 | TOP.i_can_bsp | can_bsp | default | verilog/can_top.v |
| 2 | TOP.i_can_registers.MODE_REG0 | can_register_asyn_syn | 1, 1'h1 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.MODE_REG_BASIC | can_register_asyn | 4, 0 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.MODE_REG_EXT | can_register_asyn | 3, 0 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.COMMAND_REG0 | can_register_asyn_syn | 1, 1'h0 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.COMMAND_REG1 | can_register_asyn_syn | 1, 1'h0 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.COMMAND_REG | can_register_asyn_syn | 2, 2'h0 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.COMMAND_REG4 | can_register_asyn_syn | 1, 1'h0 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.IRQ_EN_REG | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.BUS_TIMING_0_REG | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.BUS_TIMING_1_REG | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.ERROR_WARNING_REG | can_register_asyn | 8, 96 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.CLOCK_DIVIDER_REG_7 | can_register_asyn | 1, 0 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.CLOCK_DIVIDER_REG_3 | can_register_asyn | 1, 0 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.CLOCK_DIVIDER_REG_LOW | can_register_asyn | 3, 0 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.ACCEPTANCE_CODE_REG0 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.ACCEPTANCE_MASK_REG0 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG0 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG1 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG2 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG3 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG4 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG5 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG6 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG7 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG8 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG9 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG10 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG11 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.TX_DATA_REG12 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.ACCEPTANCE_CODE_REG1 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.ACCEPTANCE_CODE_REG2 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.ACCEPTANCE_CODE_REG3 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.ACCEPTANCE_MASK_REG1 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.ACCEPTANCE_MASK_REG2 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_registers.ACCEPTANCE_MASK_REG3 | can_register | 8 | verilog/can_registers.v |
| 2 | TOP.i_can_bsp.i_can_crc_rx | can_crc | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_can_acf | can_acf | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_can_fifo | can_fifo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_0 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_1 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_2 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_3 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_4 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_5 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_6 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_7 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_8 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_9 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_10 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_11 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_ibo_tx_data_12 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_calculated_crc0 | can_ibo | default | verilog/can_bsp.v |
| 2 | TOP.i_can_bsp.i_calculated_crc1 | can_ibo | default | verilog/can_bsp.v |

## 10. Conditional and unresolved resources

The active hierarchy resolves every instantiated module from the supplied RTL. No active module is unresolved. FIFO behavioral arrays are storage objects, not additional hierarchy instances.

Alternative memory branches use `lpm_ram_dp` (Altera), `actel_ram_64x8_sync`, `actel_ram_64x4_sync`, `actel_ram_64x1_sync`, Xilinx `RAMB4_S8_S8`, `RAMB4_S4_S4`, `RAMB4_S1_S1`, Virtual Silicon RAM variants, and Artisan RAM variants. Their implementation sources are not in the analyzed RTL directory. If enabled, those branches need a separate hierarchy analysis and library dependency inventory. CAN_BIST also depends on its selected memory branch and control-width macro. These conditional resources are not drawn as active blocks.

Simulation-only `timescale.v` includes refer outside the supplied RTL directory; a file was found in adjacent `bench/verilog`, and the synthesis project lists that include directory. This report does not imply that compilation was completed.

## 11. Artifact checks and provenance

- All diagram symbols, note borders, text cells and connectors were cloned exclusively from `VLSIT_DRAWIO_LIB_V1.drawio.xml` bundled with the invoked skill.
- Library SHA-256: `D1631ACF98A920526B235E8970FEDDC9305EA2F0D6A35C6529CD220D62AFABB6`.
- Template indices: 0 (text), 27 (orthogonal arrow), 32 (rectangle).
- Bundled library validator: 146 library-derived cells across three pages; checks provenance, template styles, endpoint references, complete clones and monochrome 18 pt text. It does not prove RTL semantics, geometry or protocol correctness.
- A geometry preview derived from the generated XML was inspected for layout and corrected. The native diagrams.net renderer was not available; final native rendering should be reviewed after opening the editable file.
- Hashes of the 12 module-definition source files were compared after analysis and remained unchanged; the definitions header was read without modification.

### Analyzed RTL source fingerprints

| Source | SHA-256 |
|---|---|
| verilog/can_acf.v | `404e8581e035a45b6830bba6a1e87c7899e7f54d4e3940c33ba1a25d1f20b4d6` |
| verilog/can_bsp.v | `2c3f6ed47e9f72a425c5b51980e2d0ac58640e540eb2b2a14ebe9dc2e5fc96e1` |
| verilog/can_btl.v | `7f6c42ea3d790b1643389581792ed293266d98eb0a3c1d01e6ddc777482e8335` |
| verilog/can_crc.v | `ae60397523f22b1ddcff600838949c6ded70d801d54d105ca0ad0a51013fdc07` |
| verilog/can_defines.v | `10a47046d4140f130e9bb7d161e4995d67291d33fbdb8e77903956f46bb10665` |
| verilog/can_fifo.v | `54fcf4dbfa3f0b40d24d17b758256a0e5fabe3cd45531cf2fb1a702665ae4940` |
| verilog/can_ibo.v | `4afb496a2b8e3197a5f6accaf2cb493c4ff1d8b645748dfa1a1f8535acbcc7cf` |
| verilog/can_register.v | `691454933514031ddd0f3694e1ffe68b19822ec9113b30f88dc1f2c3ca8e4fd0` |
| verilog/can_register_asyn.v | `4b83cdf224c3560f740b44d9db9d7c78e7dff6139e98685796e16baea5605561` |
| verilog/can_register_asyn_syn.v | `308ee96d28a92179915ed0ce90a8345b7b4cc4e515e245d6f00eca2fcabb9e61` |
| verilog/can_register_syn.v | `2c8b90f432acf65ed23f6b88923648f02f5e45f5727608a7011f873c633437b7` |
| verilog/can_registers.v | `ddd9d7b22c73c23c1aa52dd8e348f71a912957f963ac6dbd257a5916e0f0cae3` |
| verilog/can_top.v | `ba9f813bdee1c2d65cfa55dbf5ab9e6e33c305e30ea02b71cb9e89854bf9f921` |
