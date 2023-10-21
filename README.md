# From-2D-to-3D-Surgical-Instrument-Tracking-A-technique-based-on-intervals-and-geometric-cues


Computer-assisted interventions in minimally invasive surgery (MIS) necessitate precise motion tracking of surgical instruments. Tracking these instruments in conventional and robot-assisted MIS poses a significant challenge due to the limited availability of 2D camera projections and minimal hardware integration. This paper addresses the need to track and visualize the entire surgical instrument, including both the shaft and metallic clasper, for safe navigation within the surgical environment.

Instrument segmentation is a critical step in tracking surgical instruments. In contrast to existing methods, we introduce a 2D tracking approach based on segmentation maps of surgical instruments represented as intervals. This unique approach allows the creation of a labeled dataset without relying on ground truth information.

Motion is estimated by analyzing geometric changes within the 2D intervals, and these results are processed using kinematics-based algorithms to generate 3D tracking information. Both synthesized and experimental results for 2D and 3D motion estimates demonstrate that the method yields negligible errors, making it suitable for instrument labeling and motion tracking in various applications.

This study concludes that the proposed technique, which relies on 2D segmented intervals and their geometric transformations for 3D tracking, offers a promising, computationally efficient, and directly applicable solution to enhance regular MIS practices by enabling 3D visualization of surgical instruments.

For more information, datasets used in this research can be found in the MICCAI Endovis dataset:
(https://opencas.webarchiv.kit.edu/?q=node/30)
(https://zenodo.org/record/6362288)
(http://opencas.dkfz.de/endovis/datasetspublications/)








