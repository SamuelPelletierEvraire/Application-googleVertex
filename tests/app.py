import base64
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

def generate():
  vertexai.init(project="test-application-2-416219", location="us-central1")
  image1 = Part.from_data(data=base64.b64decode(giveImage("Images\\test1Front.jpg"))) # problème ici
  image2 = Part.from_data(data=base64.b64decode(giveImage("Images\\test1Back.png"))) # problème ici
  model = GenerativeModel("gemini-1.0-pro-vision-001")
  responses = model.generate_content(
    [image1, image2, """For each response, make a line break and put the question number.
if response = yes write true
Give the response in json and minimise the key character no capital letters
if you have no responses for the question write \"None\"
Combine the multiple picture data together to response question
When question contains Give : give the text on the bag
\"Name_of_the_registrant\": Name of manufacturer of registrant  
\"Address_of_the_registrant\": Address of manufacturer or registrant  
\"Name_of_fertilizer\": Name of fertilizer  
\"NPK_grade_designation\": A fertilizer containing major plant nutrients must include a hyphenated numerical series NPK grade designation in its name  
\"Registration_number\": Registration number  
\"Use_based_on_soil_and/or_tissue_analysis\": For micronutrient-containing products, label must indicate use based on soil and/or tissue analysis  
\"Net_weight\": Weight  
\"Measurement_unit\": Measurement are in g, kg, t?  
\"Guaranteed_analysis\": Contains the guaranteed analysis?  
\"0%_guarantees\": No 0% guarantees for contaminants ex: heavy metals or pathogens in the Guaranteed Analysis  
\"Active_Ingredients_Only\": Guaranteed Analysis: Active Ingredients Only?  
\"Minimum_N\": Minimum N % amount  
\"Minimum_P2O5\": Minimum P2O5 % amount  
\"Minimum_K2O\": Minimum K2O % amount  
\"Full_Guaranteed_analysis\": Give the full Guaranteed analysis in response  without the dots
\"Minimum_secondary_nutrient_content\": Give minimum secondary nutrient content % on elemental basis, ex: Calcium (Ca) 2%.  
\"Micronutrient_actual_amount\": Give each micronutrient actual amount %  
\"Organic_content\": If organic matter, give the minimum organic content % and maximum moisture % allowed.  
\"Maximum_moisture\": If organic matter, give the minimum organic content % and maximum moisture % allowed.  
\"Minimum_or_actual_amount_of_other_active_ingredient\": Give minimum or actual amount of other active ingredient %  
\"Concentration_per_gram\": If active ingredient amount in % is <0.001%, analysis may state concentration per gram using different unit.  
\"Pesticide_active_ingredient_concentrations\": Guaranteed analysis includes pesticide active ingredient concentrations as defined by the Pest Control Products Act, per Pest Control Products Regulations  
\"Precautionary_statements\": Give the full List of precaution in response  
\"Boron\": If Boron % >= 0,3 true  
\"Allergen\": Contains a Health Canada identified priority allergen witch on  
\"Incorrect_or_misleading_information\": No incorrect or misleading information or symbols affecting product safety, composition, or usage directions.  
\"Acronyms_define\": Used acronyms are defined  
\"Metric_imperial_units\": Units are on metric ** imperial units may appear in addition  
\"Conversion_metric_to_imperial_unit\": Conversion metric to imperial unit is accurate  
\"Lot_number\": Lot number  
\"Official_languages\": All the information that is required by the Regulations appear in both official languages French and English
\"Pest_control_product\": Claims that meet definition of pest control product  
\"Polymeric_supplement\": If contain or is polymeric supplement: Contains all necessary precautionary statements for the polymer. Directions for use conform to the conditions established by the Fertilizer Safety Section  else return None
\"Conforms_to_the_conditions\": If contain or is polymeric supplement: Contains all necessary precautionary statements for the polymer. Directions for use conform to the conditions established by the Fertilizer Safety Section else return None"""],
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 32
    },
    safety_settings={
          generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    },
    stream=True,
  )
  
  for response in responses:
    print(response.text, end="")




def giveImage(chemin_image):
    try:
        with open(chemin_image, "rb") as img_file:
            image_data = img_file.read()
            # Encoder les données de l'image en base64
            image_base64 = base64.b64encode(image_data)
            return image_base64
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")
        return None