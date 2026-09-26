# AMF-Placer — ICCAD 2021 Study Notes

**Paper:** *AMF-Placer: High-Performance Analytical Mixed-size Placer for FPGA*  
**Authors:** Tingyuan Liang, Gengjie Chen, Jieru Zhao, Sharad Sinha, Wei Zhang  
**Venue:** ICCAD 2021

This folder contains the six-day structured study notes generated while reading the paper.

## Study sequence

1. [Day 01 — Overview and Mixed-Size Placement](Day01_Overview_and_Mixed_Size_Placement.pdf)
   - FPGA Device → Site → BEL
   - standard cell vs. macro
   - four mixed-size placement challenges
   - hypergraph / HPWL formulation
   - seven-stage AMF-Placer flow

2. [Day 02 — SA Initial Placement and Quadratic Placement](Day02_SA_and_Quadratic_Placement.pdf)
   - PaToH clustering
   - coarse-bin simulated annealing
   - HPWL quadratic approximation
   - Bound2Bound model
   - anchors and pseudo nets
   - interconnection-density-aware pseudo-net weights

3. [Day 03 — Cell Spreading](Day03_Cell_Spreading.pdf)
   - resource overflow
   - macro spreading deadlock
   - resource supply fluctuation
   - utilization-guided spreading windows
   - two-phase macro spreading
   - forgetting-rate update

4. [Day 04 — Progressive Macro Legalization](Day04_Progressive_Macro_Legalization.pdf)
   - rough legalization
   - candidate-site search
   - min-cost bipartite matching
   - legalization anchors
   - exact legalization
   - column-wise dynamic programming

5. [Day 05 — Packing and Experimental Analysis](Day05_Packing_and_Experiments.pdf)
   - resource demand/supply adjustment
   - incremental packing
   - final packing
   - hash-based packing deduplication
   - ripping-up window
   - ablation and parallel speedup

6. [Day 06 — Full Review and Code-Reading Roadmap](Day06_Full_Review_and_Code_Reading_Roadmap.pdf)
   - complete algorithmic flow
   - lower-bound / upper-bound convergence
   - Tech1–Tech5 causal relationships
   - paper-to-code reading roadmap

## Main algorithmic chain

```text
SA Initial Placement
        ↓
Quadratic Placement
        ↓
Cell Spreading
        ↓
Resource Demand/Supply Adjustment
        ↓
Progressive Macro Legalization
        ↓
Incremental Packing
        ↓
Final Packing
```

## Related archives

- Google Drive archive: https://drive.google.com/drive/folders/1_uSvDDE46HfoZb2x0XOp6525dLysjlf6
- Notion page: https://app.notion.com/p/3a7106e3498e81b5abf0d1550eb73fd0?pvs=204
