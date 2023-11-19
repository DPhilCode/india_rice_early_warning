# India rice yield early warning system 
- This repo builds a rice yield early warning system, focusing on India as a case study

## Introduction

Paper II of the integrated thesis answers the  question: which algorithmic approaches are effective for crop yield forecasting, and how can these be integrated into broader early warning systems? The main contribution of this paper is to build and deploy a yield forecasting model that can predict rice yields in the major rice-growing regions of India, a region which has suffered from extreme weather events impacting foods systems. 

This paper will be closely linked to paper III (an autoethnography of agricultural early warning system model development), in that I will seek to identify and mitigate potential biases as they emerge throughout the different stages of model development. 

This work aims to build on previous efforts in the crop yield prediction literature (summarized in paper I) by building models capable of predicting rice yields at the district level for 362 districts across India. To this end, this study brings several innovations over the existing literature. 
- Firstly, an automated machine learning (AutoML) approach is applied in order to test a wide range of models, whereas previous literature has largely focused on yield prediction using a narrow range of specific algorithms such as CNNs, random forest, or support vector machine (van Klompenburg et al., 2020). 
- Secondly, a novel combination of data sources is used to predict Indian rice yields. These include data from ERA5, a climate re-analysis product developed by the European Centre for Medium Range Weather Forecasts (ECMWF), which combines observations with modelled data to provide hourly data on atmospheric, land-surface, and sea-state parameters globally (Gómez et al., 2021). Vegetation data is also derived from the MODIS sensors on-board NASA’s TERRA and AQUA satellites. 
- Thirdly, this research presents an approach capable of forecasting Indian rice yield several months prior to the end of the growing season. Lastly, this applied research discusses how the results of the yield prediction outputs could be integrated within a regional early warning system for India. 