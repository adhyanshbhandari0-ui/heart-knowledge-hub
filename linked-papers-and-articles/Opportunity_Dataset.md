# Opportunity Dataset

**Source:** https://archive.ics.uci.edu/ml/datasets/opportunity+activity+recognition

---

The OPPORTUNITY Dataset for Human Activity Recognition from Wearable, Object, and Ambient Sensors is a dataset devised to benchmark human activity recognition algorithms (classification, automatic data segmentation, sensor fusion, feature extraction, etc).

The OPPORTUNITY Dataset for Human Activity Recognition from Wearable, Object, and Ambient Sensors is a dataset devised to benchmark human activity recognition algorithms (classification, automatic data segmentation, sensor fusion, feature extraction, etc).

A subset of this dataset was used for the "OPPORTUNITY Activity Recognition Challenge" organized for the 2011 IEEE conf on Systems, Man and Cybernetics Workshop on "Robust machine learning techniques for human activity recognition". 

The dataset comprises the readings of motion sensors recorded while users executed typical daily activities:
  * Body-worn sensors: 7 inertial measurement units, 12 3D acceleration sensors, 4 3D localization information
  * Object sensors: 12 objects with 3D acceleration and 2D rate of turn
  * Ambient sensors: 13 switches and 8 3D acceleration sensors
  * Recordings: 4 users, 6 runs per users. Of these, 5 are Activity of Daily Living runs characterized by a natural execution of daily activities. The 6th run is a "drill" run, where users execute a scripted sequence of activities. 
  * Annotations/classes: the activities of the user in the scenario are annotated on different levels: "modes of locomotion" classes; low-level actions relating 13 actions to 23 objects; 17 mid-level gesture classes; and 5 high-level activity classes

** Recording scenario **

The activity recognition environment and scenario has been designed to generate many activity primitives, yet in a realistic manner. Subjects operated in a room simulating a studio flat with a deckchair, a kitchen, doors giving access to the outside, a coffee machine, a table and a chair.

We achieved a natural execution of activities by instructing users to follow a high-level script but leaving them free interpretation as how to achieve the high-level goals. We furthermore encouraged them to perform as naturally as possible with all the variations they were used to.

For each subject we recorded 6 different runs. Five of them, termed activity of daily living (ADL), followed a given scenario as detailed below. The remaining one, a drill run, was designed to generate a large number of activity instances. The ADL run consists of temporally unfolding situations. In each situation (e.g. preparing sandwich), a large number of action primitives occur (e.g. reach for bread, move to bread cutter, operate bread cutter).

* ADL run *

The ADL run consists of temporally unfolding situations:

    Start: lying on the deckchair, get up
    Groom: move in the room, check that all the objects are in the right places in the drawers and on shelves
    Relax: go outside and have a walk around the building
    Prepare coffee: prepare a coffee with milk and sugar using the coffee machine
    Drink coffee: take coffee sips, move around in the environment
    Prepare sandwich: include bread, cheese and salami, using the bread cutter and various knifes and plates
    Eat sandwich
    Cleanup: put objects used to original place or dish washer, cleanup the table
    Break: lie on the deckchair

* Drill run *

The drill run consists of 20 repetitions of the following sequence of activities:

    Open then close the fridge
    Open then close the dishwasher
    Open then close 3 drawers (at different heights)
    Open then close door 1
    Open then close door 2
    Toggle the lights on then off
    Clean the table
    Drink while standing
    Drink while seated

** Annotations **

The annotations are done on five ÃâtracksÃâ. One track contains modes of locomotion (e.g. sitting, standing, walking). Two other tracks indicate the actions of the left and right hand (e.g. reach, grasp, release), and to which object they apply (e.g. milk, switch, door).
The fourth track indicates the high level activities (e.g. prepare sandwich). The high level activities relate to the situations indicated in the description of the ADL runs as follows (in parenthesis the number of the situations indicated above): relaxing (1, 9), early morning (2, 3), coffee time (4, 5), sandwich time (6, 7), cleanup (8).

The mid-level gesture annotations is generated automatically from the low-level hand actions. It comprises coarser characterization of the user's activities. For instance the low-level annotations 'reach door' and 'open door' are combined into a single 'open door' mid-level annotation. Here, the mid-level annotations comprise actions of the left and right hand indiscriminately. However, in practice, the users mostly interacted with the environment with their right hand. We recommend to use the mid-level annotations in first attempts to use this dataset.

** Applications **

This dataset offers a rich playground to assess methods such as, e.g:

  * Classification, (semi-) supervised machine learning
  * Automatic segmentation
  * Unsupervised structure discovery
  * Data imputation
  * Multi-modal sensor fusion
  * Sensor network research
  * Transfer learning, multitask learning
  * Sensor selection
  * Feature extraction
  * Classifier calibration and adaptation
  * ...

** Baseline benchmarks **

Baseline benchmarks for the OPPORTUNITY Activity Recognition Challenge subset of the dataset are available in reference [2]. Scripts to replicate the benchmarks are provided in the package.

By D. Roggen, Alberto Calatroni, M. Rossi, Thomas Holleczek, Kilian FÃ¶rster, G. TrÃ¶ster, P. Lukowicz, D. Bannach, Gerald Pirkl, A. Ferscha, Jakob Doppler, Clemens Holzmann, Marc Kurz, G. Holl, Ricardo Chavarriaga, Hesam Sagha, Hamidreza Bayati, Marco Creatura, J. MillÃ¡n. 2010

Published in International Conference on Networked Sensing Systems

The dataset comprises the readings of motion sensors recorded while users executed typical daily activities. The detailed format is described in the package. The attributes correspond to raw sensor readings. There is a total of 242 attributes.

* Body-worn sensors (145 attributes) *

The body-worn sensors include 7 inertial measurement units and 12 3D acceleration sensors.

The inertial measurement units provide readings of: 3D acceleration, 3D rate of turn, 3D magnetic field, and orientation of the sensor with respect to a world coordinate system in quaternions. Five sensors are on the upper body and two are mounted on the user's shoes.

The acceleration sensors provide 3D acceleration. They are mounted on the upper body, hip and leg.

Four tags for an ultra-wideband localization system are placed on the left/right front/back side of the shoulder.  

* Object sensors (60 attributes) *

12 objects are instrumented with wireless sensors measuring 3D acceleration and 2D rate of turn. This allows to detect which objects are used, and possibly also the kind of usage that is made of them.

* Ambient sensors (37 attributes) *

Ambient sensors include 13 switches and 8 3D acceleration sensors in drawers, kitchen appliances and doors.

The reed switches are placed in triplets on the fridge, dishwasher and drawer 2 and drawer 3. They may be used to detect three states of the furniture element: closed, half open, and fully open. 

The acceleration sensors may allow to assess if an element of furniture is used, and whether it may be opened or closed.

This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.

This allows for the sharing and adaptation of the datasets for any purpose,
provided that the appropriate credit is given.

By using the UCI Machine Learning Repository,
you acknowledge and accept the cookies and privacy practices used by the UCI Machine Learning Repository.
