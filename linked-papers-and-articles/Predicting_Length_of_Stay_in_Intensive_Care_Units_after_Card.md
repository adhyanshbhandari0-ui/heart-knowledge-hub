# Predicting Length of Stay in Intensive Care Units after Cardiac Surgery: Comparison of Artificial Neural Networks and Adaptive Neuro-fuzzy System

**Source:** https://e-hir.org/DOIx.php?id=10.4258/hir.2018.24.2.109

---

ABOUT Aims and scope About the journal Editorial board Management policy Best practice Open access Contact us

ARTICLE CATEGORY Editorial Review article Original article Case report Tutorial Communication Others Browse all articles >

BROWSE ARTICLES Current issue All issues Most view Most download Most cited Funded articles Search Author index

FOR CONTRIBUTORS Instructions for authors Code of ethics Checklist for submission E-submission Guideline for peer review process

Healthcare Informatics Research 2018;24(2):109-117.

DOI: https://doi.org/10.4258/hir.2018.24.2.109

Predicting Length of Stay in Intensive Care Units after Cardiac Surgery: Comparison of Artificial Neural Networks and Adaptive Neuro-fuzzy System

1 Department of Health Services Management, School of Management and Medical Information Sciences, Shiraz University of Medical Sciences, Shiraz, Iran.

2 Student Research Committee, Shiraz University of Medical Sciences, Shiraz, Iran.

3 Department of Health Information Management, School of Allied Medical Sciences, Tehran University of Medical Sciences, Tehran, Iran.

4 Shiraz Anesthesiology and Critical Care Research Center, Shiraz University of Medical Sciences, Shiraz, Iran.

5 Health Human Resources Research Centre, School of Management and Medical Information Sciences, Shiraz University of Medical Sciences, Shiraz, Iran.

Corresponding Author: Ramin Ravangard, PhD. Department of Health Services Management, School of Management and Medical Information Sciences, Shiraz University of Medical Sciences, Shiraz, Iran. Tel: +987132340774, ra_ravangard@yahoo.com

Â© 2018 The Korean Society of Medical Informatics

Objectives Accurate prediction of patients' length of stay is highly important. This study compared the performance of artificial neural network and adaptive neuro-fuzzy system algorithms to predict patients' length of stay in intensive care units (ICU) after cardiac surgery. Methods A cross-sectional, analytical, and applied study was conducted. The required data were collected from 311 cardiac patients admitted to intensive care units after surgery at three hospitals of Shiraz, Iran, through a non-random convenience sampling method during the second quarter of 2016. Following the initial processing of influential factors, models were created and evaluated. Results The results showed that the adaptive neuro-fuzzy algorithm (with mean squared error [MSE] = 7 and R = 0.88) resulted in the creation of a more precise model than the artificial neural network (with MSE = 21 and R = 0.60). Conclusions The adaptive neuro-fuzzy algorithm produces a more accurate model as it applies both the capabilities of a neural network architecture and experts' knowledge as a hybrid algorithm. It identifies nonlinear components, yielding remarkable results for prediction the length of stay, which is a useful calculation output to support ICU management, enabling higher quality of administration and cost reduction.

Keywords : Forecasting , Neural Networks , Decision Support Techniques , Length of Stay , Heart Diseases , Cardiac Surgical Procedures , Intensive Care Unit

1. Identification of the Factors Affecting the Length of Stay in Intensive Care Units

2. Data Collection Based on Variables and Identified Factors

4. Conversion of Electronic Dataset to Learning and Test Datasets

6. Error Calculation and Comparison of Model Performance

Conflict of Interest: No potential conflict of interest relevant to this article was reported.

A part of the CART decision tree induced by 32 variables. In the decision tree, X = (x 1 ,â¦, x 32 ) are introduced as follows: x 1 = age, x 2 = gender, x 3 = surgery type, x 4 = hematocrit, x 5 = type of operation, x 6 = duration CPB, x 7 = clamp time, x 8 = LVEF, x 10 = renal disease, x 11 = reoperation, x 13 = hypertension, x 17 = OPCAB, x 19 = CPB, x 20 = sinus rhythm, x 21 = myocardial infarction, x 22 = mild valvulopathy, x 24 = NYHA, x 25 = creatinine, x 27 = MIDCAB, x 28 = HVS, x 29 = hypercholesterolemia, x 30 = preoperative infection, x 32 = BMI. As an example inducted rule from decision tree: IF x 8 < 3 AND x 27 < 1.5 THEN length of stay = 11.2. CPB: cardiopulmonary bypass, LVEF: left ventricular ejection fraction, OPCAB: off-pump coronary artery bypass, NYHA: New York Heart Association, MIDCAB: minimally invasive direct coronary artery bypass, HVS: heart valve surgery, BMI: body mass index.

Descriptive information of factors influencing length of stay in ICU after cardiac surgery for patients considered in this study

ICU: intensive care unit, LVEF: left ventricular ejection fraction, TIA: transient ischemic attack, MIDCAB: minimally invasive direct coronary artery bypass, COPD: chronic obstructive pulmonary disease, CABG: coronary artery bypass graft, MVR: mitral valve replacement, AVR: aortic valve replacement, CPB: cardiopulmonary bypass, NYHA: New York Heart Association, OPCAB: off-pump coronary artery bypass.

Quantitative variables which positively affected studied patients' length of stay after cardiac surgery

Values are presented as mean Â± standard deviation.

BMI: body mass index, CPB: cardiopulmonary bypass.

Results of MLP ANN evaluation based on calculated R for various numbers of neurons in hidden layers of the neural networks structures learned by training, testing, validation, and whole datasets

MLP: multi-layer perceptron, ANN: artificial neural network.

Comparison of R and MSE as model assessment criteria for data learning using ANNs and ANFIS algorithms

MSE: mean squared error, ANN: artificial neural network, ANFIS: adaptive neuro-fuzzy inference system.

Copyright © 2026 by Korean Society of Medical Informatics.
