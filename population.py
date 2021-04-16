import pandas as pd
import numpy as np
import streamlit as st

class Population_Data:

    # population data is taken from the following site and has been manually entered and later added to the country data frame through following defined function - Refer https://www.worldometers.info/world-population/population-by-country/ 
    
    @staticmethod
    @st.cache
    def population_list():
        population = {
            38928346: "Afghanistan",
            2877797:"Albania",
            43851044:"Algeria",
            77265:"Andorra",
            32866272:"Angola",
            97929:"Antigua and Barbuda",
            45195774:"Argentina",
            2963243:"Armenia",
            25499884:"Australia",
            9006398:"Austria",
            10139177:"Azerbaijan",
            393244:"Bahamas",
            1701575:"Bahrain",
            164689383:"Bangladesh",
            287375:"Barbados",
            9449323:"Belarus",
            11589623:"Belgium",
            397628:"Belize",
            12123200:"Benin",
            771608:"Bhutan",
            11673021:"Bolivia",
            3280819:"Bosnia and Herzegovina",
            2351627:"Botswana",
            212559417:"Brazil",
            437479:"Brunei",
            6948445:"Bulgaria",
            20903273:"Burkina Faso",
            54409800:"Burma",
            1189784:"Burundi",
            555987:"Cabo Verde",
            16718965:"Cambodia",
            26545863:"Cameroon",
            37742154:"Canada",
            4829767:"Central African Republic",
            16425864:"Chad",
            19116201:"Chile",
            1439323776:"China",
            50882891:"Colombia",
            869601:"Comoros",
            5380508:"Congo (Brazzaville)",
            86790567:"Congo (Kinshasa)",
            5094118:"Costa Rica",
            26378274:"Cote d'Ivoire",
            4105267:"Croatia",
            11326616:"Cuba",
            1207359:"Cyprus",
            10708981:"Czechia",
            5792202:"Denmark",
            988000:"Djibouti",
            71986:"Dominica",
            10847910:"Dominican Republic",
            17643054:"Ecuador",
            102334404:"Egypt",
            6486205:"El Salvador",
            1402985:"Equatorial Guinea",
            3546421:"Eritrea",
            1326535:"Estonia",
            1160164:"Eswatini",
            114963588:"Ethiopia",
            896445:"Fiji",
            5540720:"Finland",
            65273511:"France",
            2225734:"Gabon",
            2416668:"Gambia",
            3989167:"Georgia",
            83783942:"Germany",
            31072940:"Ghana",
            10423054:"Greece",
            112523:"Grenada",
            17915568:"Guatemala",
            13132795:"Guinea",
            1968001:"Guinea-Bissau",
            786552:"Guyana",
            11402528:"Haiti",
            801:"Holy See",
            9904607:"Honduras",
            9660351:"Hungary",
            341243:"Iceland",
            1380004385:"India",
            273523615:"Indonesia",
            83992949:"Iran",
            40222493:"Iraq",
            4937786:"Ireland",
            8655535:"Israel",
            60461826:"Italy",
            2961167:"Jamaica",
            126476461:"Japan",
            10203134:"Jordan",
            18776707:"Kazakhstan",
            53771296:"Kenya",
            51269185:"Korea, South",
            1767881:"Kosovo",
            4270571:"Kuwait",
            6524195:"Kyrgyzstan",
            7275560:"Laos",
            1886198:"Latvia",
            6825445:"Lebanon",
            2142249:"Lesotho",
            5057681:"Liberia",
            6871292:"Libya",
            38128:"Liechtenstein",
            2722289:"Lithuania",
            625978:"Luxembourg",
            27691018:"Madagascar",
            19129952:"Malawi",
            32365999:"Malaysia",
            540544:"Maldives",
            20250833:"Mali",
            441543:"Malta",
            59190:"Marshall Islands",
            4649658:"Mauritania",
            1271768:"Mauritius",
            128932753:"Mexico",
            548914:"Micronesia",
            4033963:"Moldova",
            39242:"Monaco",
            3278290:"Mongolia",
            628066:"Montenegro",
            36910560:"Morocco",
            31255435:"Mozambique",
            2540905:"Namibia",
            29136808:"Nepal",
            17134872:"Netherlands",
            4822233:"New Zealand",
            6624554:"Nicaragua",
            24206644:"Niger",
            206139589:"Nigeria",
            2083374:"North Macedonia",
            5421241:"Norway",
            5106626:"Oman",
            220892340:"Pakistan",
            4314767:"Panama",
            8947024:"Papua New Guinea",
            7132538:"Paraguay",
            32971854:"Peru",
            109581078:"Philippines",
            37846611:"Poland",
            10196709:"Portugal",
            2881053:"Qatar",
            19237691:"Romania",
            145934462:"Russia",
            12952218:"Rwanda",
            53199:"Saint Kitts and Nevis",
            183627:"Saint Lucia",
            110940:"Saint Vincent and the Grenadines",
            198414:"Samoa",
            33931:"San Marino",
            219159:"Sao Tome and Principe",
            34813871:"Saudi Arabia",
            16743927:"Senegal",
            8737371:"Serbia",
            98347:"Seychelles",
            7976983:"Sierra Leone",
            5850342:"Singapore",
            5459642:"Slovakia",
            2078938:"Slovenia",
            686884:"Solomon Islands",
            15893222:"Somalia",
            59308690:"South Africa",
            11193725:"South Sudan",
            46754778:"Spain",
            21413249:"Sri Lanka",
            43849260:"Sudan",
            586632:"Suriname",
            10099265:"Sweden",
            8654622:"Switzerland",
            17500658:"Syria",
            23816775:"Taiwan*",
            9537645:"Tajikistan",
            59734218:"Tanzania",
            69799978:"Thailand",
            1318445:"Timor-Leste",
            8278724:"Togo",
            1399488:"Trinidad and Tobago",
            11818619:"Tunisia",
            84339067:"Turkey",
            331002651:"US",
            45741007:"Uganda",
            43733762:"Ukraine",
            9890402:"United Arab Emirates",
            67886011:"United Kingdom",
            3473730:"Uruguay",
            33469203:"Uzbekistan",
            30145:"Vanuatu",
            28435940:"Venezuela",
            97338579:"Vietnam",
            5101414:"West Bank and Gaza",
            29825964:"Yemen",
            18383955:"Zambia",
            14862924:"Zimbabwe"
            }

        return population
