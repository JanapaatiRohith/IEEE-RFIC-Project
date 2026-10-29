** adapted from:
** sch_path: ihp-sg13g2/libs.tech/xschem/sg13g2_tests/ac_hbt_13g2.sch
**.subckt ac_hbt_13g2
Vce net2 GND 5
XQ1 Vc Vb GND GND npn13G2 Nx=1 selft=0
R1 net2 Vc 40k m=1
Vce1 net1 GND dc 0.8 ac 1m
R2 Vb net1 33k m=1
**** begin user architecture code

.lib cornerHBT.lib hbt_typ

.param temp=27
.control
save v(vc) v(vb)
ac dec 100 10k 100meg
set wr_vecnames
set wr_singlescale
wrdata /mnt/c/IEEE_RFIC_Project/simulation_results/hbt_ac_typ_dense.dat mag(v(vc)) mag(v(vb))
.endc


**** end user architecture code
**.ends
.GLOBAL GND
.end
