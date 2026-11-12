# Artificial Intelligence Improves Accuracy of Heart Failure Readmission Risk Predictions

**Source:** https://www.healthcatalyst.com/success_stories/machine-learning-in-heart-failure-multicare

---

Artificial Intelligence Improves Accuracy of Heart Failure Readmission Risk Predictions

In the U.S., 5.7 million adults have heart failure (HF), costing the nation an estimated $30.7 billion each year. Learn how MultiCare leveraged AI and machine learning to more accurately predict the readmission risk for patients with HF.

A global pandemic, heart failure (HF) affects at least 26 million people worldwide, and its prevalence only continues to increase. Within the U.S. alone, 5.7 million adults live with HF, carrying a cost of nearly $30.7 billion each year. At 55 percent, HF represents the most common cause of Medicare readmissions, and HF accounts for 42 percent of total admissions for Medicare patients.

Readmissions for HF carry a heavy cost for patients and health systems, in addition to reimbursement penalties from CMS. This makes properly assessing the risk for readmission for patients with HF a top priority. MultiCare Health System leveraged artificial intelligence and machine learning to improve the accuracy of readmission risk predictions for patients with HF. Providing a more accurate risk score in a timely fashion gives care teams more time to intervene effectively and prevent avoidable readmissions.

HEART FAILURE READMISSIONS CARRY HEAVY COST

Heart failure (HF) affects over 26 million people worldwide. Already a global pandemic, rates of HF continue to increase. 1 Within the U.S., 5.7 million adults have HF, costing the nation an estimated $30.7 billion each year. 2 Patients with HF represent 42 percent of all Medicare admissions, and 55 percent of all Medicare readmissions, making HF the most common condition associated with a Medicare readmission. 3

Healthcare organizations that wish to prevent avoidable readmission, and avoid penalties from CMS’s readmission reduction program, need to be able to get upstream of the readmission event by accurately predicting which patients are at the highest risk for readmission, and then align resources and support to prevent an avoidable readmission.

Many organizations use the LACE index (length of stay, acuity of admission, Charlson comorbidity index (CCI), and number of emergency department visits in the preceding six months) to predict a patient’s risk for readmission. The LACE index was created using data from 4,812 patients admitted to 11 hospitals in Canada between October 2002 and July 2006. 2 While it is widely used, the LACE index was developed using data from middle-aged Canadian patients who did not have serious comorbidities. Due to this limitation, critics have questioned the validity of the LACE index in its applicability to broader patient populations. 4, 5

MultiCare is a not-for-profit healthcare organization made up of numerous primary care, urgent care, and specialty services. MultiCare’s comprehensive healthcare system also includes eight hospitals that serve the Pacific Northwest and the Pulse Heart Institute (Pulse Heart). Pulse Heart strives to be the Pacific Northwest’s destination for adult heart health, offering a comprehensive range of the most advanced cardiac, thoracic, and vascular services available.

MultiCare and Pulse Heart are committed to standardizing and providing the best care to its patients with HF to improve the overall quality of care and outcomes for its patients, believing that this will ultimately result in a change in the patient’s course for the chronic condition, effectively reducing hospitalizations, readmissions, and mortality.

ASSESSING HEART FAILURE READMISSION RISK LIMITED BY DATA ACCESS AND MANUAL ENTRY ISSUES

The Pulse Heart HF center of excellence is a collective coalition representing the multiple disciplines and facets of healthcare that touch each of its patients with HF. Pulse Heart and the HF center of excellence established evidence-based guidelines for the treatment of HF at MultiCare, outlining the expected medical management of these patients. These guidelines incorporate national guidelines from the American Heart Association and American College of Cardiology, providing guidance for each aspect of the patient’s care, from initial diagnosis to ongoing medical management in both the outpatient and inpatient settings—including advanced care planning, palliative care, and home assistance.

Included in the discharge planning section of the guideline are criteria for discharge and considerations regarding the timeliness of follow-up appointments for patients at high risk for readmission. To be most accurate, the patient’s risk for readmission should be calculated on admission and throughout the patient’s stay, with the data being used to develop the patient’s medical treatment plan. Because the risk for readmission was calculated after manual data entry by the clinician and determined using information that was sometimes difficult to locate in the EHR, it was challenging to ensure the accuracy of the risk prediction, decreasing the utility of any assessment.

Additionally, determining the risk of readmission at admission did not always result in appropriate allocation of the right outpatient resources, as patients’ needs often change and new information emerges during the hospital admission. This limited the ability to ensure appropriate aftercare and follow-up appointments to prevent an avoidable, costly readmission. To further reduce readmissions, MultiCare and Pulse Heart sought to improve the timeliness and accuracy of its readmission risk predictions for patients with HF, providing the care team adequate time to intervene and prevent avoidable readmissions.

MACHINE LEARNING IN HEART FAILURE IMPROVES READMISSION RISK PREDICTION

To improve the accuracy and timeliness of its risk prediction model, MultiCare and Pulse Heart partnered with Health Catalyst, leveraging the Health Catalyst ® Data Operating System (DOS™) platform and Healthcare.AI™, to develop a HF 30-day readmission risk-prediction model that utilizes MultiCare’s historical data to determine the probability of currently admitted patients being readmitted within 30-days of discharge.

To develop the predictive model, the center of excellence used an iterative process to identify variables, guiding the development of the model and validating results.

Stakeholders considered 87 different variables for inclusion in the predictive model. Health Catalyst’s data scientists and analytics engineers used an iterative feature selection and the random forest’s Gini impurity index to determine which variables remained in the final model. Ultimately, 25 variables selected as those that had the highest area under the curve (AUROC: measure of quality for classification models) were selected for use in the model. The selected variables accounted for the most significant impact on HF readmission prediction.

The HF 30-day readmission risk prediction model is integrated into the Heart Failure analytics accelerator. In addition to visualizing 30−day readmission performance, LOS, emergency department utilization, and observation stays for patients with HF, the analytics application provides a visualization of the readmission risk level for MultiCare’s currently admitted patients who have HF as a primary diagnosis. The risk score in the analytics application is updated daily, as a patient’s clinical indicators change throughout their stay, and stratified based on discussions with stakeholders and domain experts, grouping patients into several different risk categories:

Risk prediction and stratification are provided on two levels within the analytics application:

At the population level, to provide an overview of currently admitted patient risk levels.

At the patient level, to support patient-level interventions.

MultiCare implemented standard work, utilizing the HF 30-day readmission risk prediction to further improve the overall quality of care and outcomes for its patients. Each day, a nurse uses a risk-stratified worklist in the analytics application, focusing first on the patients with the highest risk for readmission, confirming all patients understand the discharge plan and have a timely follow-up appointment scheduled after discharge, especially if they are at high risk for readmission.

As the work progresses, clinicians will monitor patients using the worklist and patient details in the EHR, initiating evidence-based interventions in the HF guidelines to effectively manage the patient’s HF, including interventions to maximize the patient’s functional status and reduce the risk for an avoidable, costly readmission within 30-days of discharge.

By engaging stakeholders from across the organization and utilizing artificial intelligence and machine learning, MultiCare and Pulse Heart have successfully implemented a predictive model that is more accurate than similar nationally recognized models.

The AUROC for the HF 30-day readmission risk prediction model is 0.85 (LACE predicts readmissions with an AUROC around 0.62). The true-positive rate (sensitivity) is 0.84, and the false-positive rate is 0.24. The AUROC is a measure of quality for classification models, measuring the ability of the model to correctly predict which patients will be readmitted.

The AUROC is a measure of quality for classification models, measuring the ability of the model to correctly predict which patients will be readmitted.

Classification systems that cannot distinguish between two groups have an AUC (area under the curve) equal to 0.5. An AUC of 0.80-0.90 is considered good performance, meaning that HF 30-day readmission risk prediction model is good at separating which patients will be readmitted, and which patients will not.

Additionally, MultiCare has achieved specific improvements in its risk predictions, including:

Improved accuracy of risk-prediction data used by clinicians to inform the medical treatment plan, discharge plan, and after hospital follow-up.

Risk predictions are now available daily, instead of on admission only. Improved timeliness and accuracy of the risk predictions have improved the clinicians’ ability to provide patient-specific interventions, decreasing the likelihood of an avoidable readmission.

Three-fold increase in the number of HF readmission risk predictions made each day. Approximately 150 HF readmission risk predictions are made daily.

MultiCare plans to employ closed-loop analytics to integrate the risk data into MultiCare’s EHR, at which point clinicians, operational leaders, and executives will use the population-level risk data to monitor the currently admitted population’s high-level risk trends. After reviewing patient-specific data, including the top three risk factors contributing to the patient’s risk for readmission, clinicians will document the care provided to manage their HF and the interventions taken to prevent an avoidable, costly readmission.

MultiCare and Pulse Heart plan to continue to look for opportunities to employ artificial intelligence and predictive analytics to improve the care provided to its patients, continuing its journey to effectively reduce hospitalizations, readmissions, and mortality from HF.

Savarese, G., & Lund, L. H. (2017). Global public health burden of heart failure . Cardiac Failure Review, 3 (1), 7-11.

Centers for Disease Control and Prevention. (2016). Heart failure fact sheet .

Fitch, K., Pelizzari, P. M., & Pyenson, B. (2015). The high cost of heart failure for the Medicare population: An actuarial cost analysis .

Cotter, P. E., Bhalla, V. K., Wallis, S. J., & Biram, R. W. (2012). Predicting readmissions: Poor performance of the LACE index in an older UK population . Age Ageing, 41 (6), 784-89.

Tan, S. Y., Low, L. L., Yang, Y., & Lee, K. H. (2013). Applicability of a previously validated readmission predictive index in medical patients in Singapore: A retrospective study . BMC Health Serv Res., 13 , 366.

The AUROC (area under the curve of the receiver operating characteristic) for the HF 30-day readmission risk prediction model is 0.85 (LACE predicts readmissions with an AUROC around 0.62).

Three-fold increase in the number of HF readmission risk predictions made each day.
