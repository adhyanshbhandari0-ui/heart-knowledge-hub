# Prediction of cardiovascular outcomes with machine learning techniques: application to the CORAL study
- **Authors:** Tian Chen, Pamela Brewster, Katherine R Tuttle, Lance Dworkin, Joseph I Shapiro, et al.
- **Journal:** International Journal of Nephrology and Renovascular Disease (March 2019, 12:49-58)
- **DOI:** 10.2147/IJNRD.S194727

## Key Findings
- Analyzed 573 CORAL subjects with complete baseline data (80:20 train/test split across 10 seeds using R CARET).
- Models tested: GLM (62.7% ROC), SVM (65.3% ROC), Decision Tree/RPART (53.0% ROC), Neural Network (63.1% ROC), Random Forest (68.1% ± 4.3% ROC).
- Top predictors in Random Forest: Systolic BP (SBP), Serum Creatinine, Glycosylated Hemoglobin (HbA1c), Diastolic BP (DBP).
- Treatment assignment (stenting vs. medical therapy alone) was not an important predictor in any model.
