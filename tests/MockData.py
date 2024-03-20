from unittest.mock import Mock


def create_mock_data1():
    mock_data = Mock()
    mock_data.Name_of_the_registrant = "Golfgreen Organic"
    mock_data.Address_of_the_registrant = "1655 Aimco Blvd, Milton, ON L9T 6H6"
    mock_data.Name_of_fertilizer = "Golfgreen Organic Compost Manure with Peat Moss"
    mock_data.NPK_grade_designation = "0.5-0.5-0.5"
    mock_data.Registration_number = "159020424"
    mock_data.Use_based_on_soil_and_or_tissue_analysis = True
    mock_data.Net_weight = "15"
    mock_data.Measurement_unit = "kg"
    mock_data.Guaranteed_analysis = True
    mock_data.No_Guarantees = True
    mock_data.Active_Ingredients_Only = True
    mock_data.Minimum_N = "0.5"
    mock_data.Minimum_P2O5 = "0.5"
    mock_data.Minimum_K2O = "0.5"
    mock_data.Full_Guaranteed_analysis = "Nitrogen (N).......................0.5%\nAvailable Phosphorous (P2O5)....0.5%\nSoluble Potassium (K2O)..........0.5%\nOrganic Matter.........................65.0%\nMaximum Moisture..................40.0%"
    mock_data.Minimum_secondary_nutrient_content = "Calcium (Ca) 2%\nMagnesium (Mg) 0.6%\nSulphur (S) 0.6%"
    mock_data.Micronutrient_actual_amount = "Iron (Fe) 0.3%\nManganese (Mn) 0.06%\nZinc (Zn) 0.02%"
    mock_data.Organic_content = "Organic Matter.........................65.0%\nMaximum Moisture..................40.0%"
    mock_data.Maximum_moisture = "Organic Matter.........................65.0%\nMaximum Moisture..................40.0%"
    mock_data.Minimum_or_actual_amount_of_other_active_ingredient = None
    mock_data.Concentration_per_gram = None
    mock_data.Pesticide_active_ingredient_concentrations = False
    mock_data.Precautionary_statements = "KEEP OUT OF REACH OF CHILDREN\nHARMFUL IF SWALLOWED\nAvoid contact with eyes, skin and clothing. Wash hands thoroughly after use. Do not breathe dust."
    mock_data.Boron = False
    mock_data.Allergen = False
    mock_data.Incorrect_or_misleading_information = True
    mock_data.Acronyms_define = True
    mock_data.Metric_imperial_units = True
    mock_data.Conversion_metric_to_imperial_unit = True
    mock_data.Lot_number = "L18248A"
    mock_data.Official_languages = True
    mock_data.Pest_control_product = False
    mock_data.Polymeric_supplement = False
    mock_data.Conforms_to_the_conditions = True

    return mock_data

def convert_mock_to_dict(mock_data):
    mock_dict = {}
    for attr_name in dir(mock_data):
        if not attr_name.startswith("__"):
            attr_value = getattr(mock_data, attr_name)
            mock_dict[attr_name] = attr_value
    return mock_dict