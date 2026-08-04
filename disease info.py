# Dictionary mapping disease classes to metadata, treatment advice, and translations in Tamil and English
DISEASE_DATA = {
    'Tomato___Bacterial_spot': {
        'name_en': 'Tomato - Bacterial Spot',
        'name_ta': 'தக்காளி - பாக்டீரியல் புள்ளி நோய்',
        'advice_en': 'Use copper-based fungicides. Remove and destroy infected plant debris. Avoid overhead watering to reduce wetness on leaves. Plant resistant varieties if available.',
        'advice_ta': 'செம்பு சார்ந்த பூஞ்சைக் கொல்லிகளைப் பயன்படுத்தவும். பாதிக்கப்பட்ட தாவரக் கழிவுகளை அகற்றி அழிக்கவும். இலைகளில் ஈரப்பதத்தைக் குறைக்க இலைகளின் மேல் தண்ணீர் தெளிப்பதைத் தவிர்க்கவும். நோய் எதிர்ப்புத் திறன் கொண்ட ரகங்களை நடவு செய்யவும்.',
        'is_healthy': False
    },
    'Tomato___Early_blight': {
        'name_en': 'Tomato - Early Blight',
        'name_ta': 'தக்காளி - ஆரம்ப கருகல் நோய்',
        'advice_en': 'Apply fungicides containing chlorothalonil or copper. Prune lower leaves to improve air circulation. Keep soil mulched to prevent fungal spores from splashing up.',
        'advice_ta': 'குளோரோதலோனில் அல்லது செம்பு கொண்ட பூஞ்சைக் கொல்லிகளைப் பயன்படுத்தவும். காற்று ஓட்டத்தை மேம்படுத்த கீழ் இலைகளை கவாத்து செய்யவும். பூஞ்சை வித்திகள் மேலே தெளிப்பதைத் தடுக்க மண்ணை தழைக்கூளம் கொண்டு மூடவும்.',
        'is_healthy': False
    },
    'Tomato___Late_blight': {
        'name_en': 'Tomato - Late Blight',
        'name_ta': 'தக்காளி - பிற்கால கருகல் நோய்',
        'advice_en': 'Destructive disease! Apply preventative fungicides immediately (chlorothalonil, mancozeb). Destroy infected plants to stop the spread. Avoid high humidity where possible.',
        'advice_ta': 'அழிவு தரும் நோய்! உடனடியாக பூஞ்சைக் கொல்லிகளைப் பயன்படுத்தவும் (குளோரோதலோனில், மேங்கோசெப்). பரவுவதை நிறுத்த பாதிக்கப்பட்ட தாவரங்களை அழிக்கவும். முடிந்தவரை அதிக ஈரப்பதத்தைத் தவிர்க்கவும்.',
        'is_healthy': False
    },
    'Tomato___Leaf_Mold': {
        'name_en': 'Tomato - Leaf Mold',
        'name_ta': 'தக்காளி - இலை பூஞ்சை காளான்',
        'advice_en': 'Improve greenhouse ventilation and air circulation around plants. Avoid overhead irrigation. Apply fungicides if infection is severe.',
        'advice_ta': 'தாவரங்களைச் சுற்றி பசுமைக்குடில் காற்றோட்டம் மற்றும் காற்றுச் சுழற்சியை மேம்படுத்தவும். இலைகளின் மேல் நீர்ப்பாசனம் செய்வதைத் தவிர்க்கவும். தொற்று கடுமையாக இருந்தால் பூஞ்சைக் கொல்லிகளைப் பயன்படுத்தவும்.',
        'is_healthy': False
    },
    'Tomato___Septoria_leaf_spot': {
        'name_en': 'Tomato - Septoria Leaf Spot',
        'name_ta': 'தக்காளி - செப்டோரியா இலைப்புள்ளி நோய்',
        'advice_en': 'Remove infected leaves. Apply organic fungicides. Practice crop rotation and clear weeds around the garden. Keep watering restricted to the base of the plant.',
        'advice_ta': 'பாதிக்கப்பட்ட இலைகளை அகற்றவும். இயற்கை பூஞ்சைக் கொல்லிகளைப் பயன்படுத்தவும். பயிர் சுழற்சியைப் பயிற்சி செய்யவும் மற்றும் தோட்டத்தைச் சுற்றியுள்ள களைகளை அகற்றவும். செடியின் அடிப்பகுதிக்கு மட்டும் தண்ணீர் ஊற்றவும்.',
        'is_healthy': False
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'name_en': 'Tomato - Two-Spotted Spider Mite',
        'name_ta': 'தக்காளி - இருப்புள்ளி சிலந்திப் பூச்சி',
        'advice_en': 'Spray plants with water to knock off mites. Apply insecticidal soap or neem oil. Encourage natural predators like ladybugs.',
        'advice_ta': 'சிலந்திகளை அகற்ற தாவரங்கள் மீது தண்ணீரை தெளிக்கவும். பூச்சிக்கொல்லி சோப் அல்லது வேப்பெண்ணெய் பயன்படுத்தவும். பொன்வண்டுகள் போன்ற இயற்கையான வேட்டையாடும் பூச்சிகளை ஊக்குவிக்கவும்.',
        'is_healthy': False
    },
    'Tomato___Target_Spot': {
        'name_en': 'Tomato - Target Spot',
        'name_ta': 'தக்காளி - இலக்கு புள்ளி நோய்',
        'advice_en': 'Apply appropriate fungicides (chlorothalonil). Maintain plant spacing for airflow. Keep plants staked and pruned off the ground.',
        'advice_ta': 'பொருத்தமான பூஞ்சைக் கொல்லிகளைப் பயன்படுத்தவும் (குளோரோதலோனில்). காற்று ஓட்டத்திற்காக தாவர இடைவெளியை பராமரிக்கவும். தாவரங்களை குச்சிகளால் கட்டி தரையிலிருந்து தூக்கி வைக்கவும்.',
        'is_healthy': False
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'name_en': 'Tomato - Yellow Leaf Curl Virus',
        'name_ta': 'தக்காளி - மஞ்சள் இலை சுருள் வைரஸ்',
        'advice_en': 'Transmitted by whiteflies. Control whiteflies using neem oil or yellow sticky traps. Cover crops with fine netting. Remove infected plants immediately.',
        'advice_ta': 'வெள்ளை ஈக்களால் பரவுகிறது. வேப்பெண்ணெய் அல்லது மஞ்சள் பசை பொறிகளைப் பயன்படுத்தி வெள்ளை ஈக்களைக் கட்டுப்படுத்தவும். பயிர்களை மெல்லிய வலையால் மூடவும். பாதிக்கப்பட்ட தாவரங்களை உடனடியாக அகற்றவும்.',
        'is_healthy': False
    },
    'Tomato___Tomato_mosaic_virus': {
        'name_en': 'Tomato - Mosaic Virus',
        'name_ta': 'தக்காளி - மொசைக் வைரஸ்',
        'advice_en': 'No cure exists. Pull out and burn infected plants. Wash hands and tools with soap after handling. Do not smoke near plants (transmits tobacco mosaic virus).',
        'advice_ta': 'இதற்கு தீர்வு இல்லை. பாதிக்கப்பட்ட தாவரங்களை பிடுங்கி எரிக்கவும். கையாண்ட பிறகு கைகளையும் கருவிகளையும் சோப்பால் கழுவவும். தாவரங்களுக்கு அருகில் புகைபிடிக்க வேண்டாம் (புகையிலை மொசைக் வைரஸ் பரவும்).',
        'is_healthy': False
    },
    'Tomato___healthy': {
        'name_en': 'Tomato - Healthy Leaf',
        'name_ta': 'தக்காளி - ஆரோக்கியமான இலை',
        'advice_en': 'Your plant leaf is completely healthy! Continue regular watering, proper fertilization, and ensure adequate sunlight.',
        'advice_ta': 'உங்கள் தாவர இலை முற்றிலும் ஆரோக்கியமாக உள்ளது! வழக்கமான நீர்ப்பாசனம், சரியான உரமிடுதல் மற்றும் போதுமான சூரிய ஒளி கிடைப்பதை உறுதிசெய்யவும்.',
        'is_healthy': True
    },
    'Potato___Early_blight': {
        'name_en': 'Potato - Early Blight',
        'name_ta': 'உருளைக்கிழங்கு - ஆரம்ப கருகல் நோய்',
        'advice_en': 'Practice crop rotation. Apply copper fungicides. Ensure proper nutrition (nitrogen and phosphorus) to keep plants vigorous.',
        'advice_ta': 'பயிர் சுழற்சியைப் பயிற்சி செய்யவும். செம்பு பூஞ்சைக் கொல்லிகளைப் பயன்படுத்தவும். தாவரங்கள் வீரியமாக இருக்க சரியான ஊட்டச்சத்தை (நைட்ரஜன் மற்றும் பாஸ்பரஸ்) உறுதி செய்யவும்.',
        'is_healthy': False
    },
    'Potato___Late_blight': {
        'name_en': 'Potato - Late Blight',
        'name_ta': 'உருளைக்கிழங்கு - பிற்கால கருகல் நோய்',
        'advice_en': 'High humidity fuels this blight. Apply preventative fungicides (mancozeb, chlorothalonil) weekly in wet conditions. Plant certified disease-free tubers.',
        'advice_ta': 'அதிக ஈரப்பதம் இந்த நோயை ஊக்குவிக்கிறது. ஈரமான நிலையில் வாரந்தோறும் தடுப்பு பூஞ்சைக் கொல்லிகளை (மேங்கோசெப், குளோரோதலோனில்) பயன்படுத்தவும். சான்றளிக்கப்பட்ட நோய் இல்லாத கிழங்குகளை நடவும்.',
        'is_healthy': False
    },
    'Potato___healthy': {
        'name_en': 'Potato - Healthy Leaf',
        'name_ta': 'உருளைக்கிழங்கு - ஆரோக்கியமான இலை',
        'advice_en': 'Your potato leaf is healthy. Keep soil moisture stable and inspect regularly for pest damage.',
        'advice_ta': 'உங்கள் உருளைக்கிழங்கு இலை ஆரோக்கியமாக உள்ளது. மண் ஈரப்பதத்தை சீராக வைத்துக்கொள்ளவும், பூச்சி சேதம் உள்ளதா என தொடர்ந்து ஆய்வு செய்யவும்.',
        'is_healthy': True
    },
    'Pepper__bell___Bacterial_spot': {
        'name_en': 'Bell Pepper - Bacterial Spot',
        'name_ta': 'குடைமிளகாய் - பாக்டீரியல் புள்ளி நோய்',
        'advice_en': 'Apply copper-based sprays early. Rotate crops every 2-3 years. Avoid working in wet fields to prevent spreading bacterial pathogens.',
        'advice_ta': 'ஆரம்பத்திலேயே செம்பு சார்ந்த தெளிப்பான்களைப் பயன்படுத்தவும். 2-3 ஆண்டுகளுக்கு ஒருமுறை பயிர்களை சுழற்சி முறையில் பயிரிடவும். பாக்டீரியா நோய்க்கிருமிகள் பரவுவதைத் தடுக்க ஈரமான வயல்களில் வேலை செய்வதைத் தவிர்க்கவும்.',
        'is_healthy': False
    },
    'Pepper__bell___healthy': {
        'name_en': 'Bell Pepper - Healthy Leaf',
        'name_ta': 'குடைமிளகாய் - ஆரோக்கியமான இலை',
        'advice_en': 'The pepper leaf is in excellent condition. Ensure it receives full sun and has well-draining soil.',
        'advice_ta': 'மிளகு இலை சிறந்த நிலையில் உள்ளது. முழு சூரிய ஒளி மற்றும் வடிகால் வசதியுள்ள மண் கிடைப்பதை உறுதி செய்யவும்.',
        'is_healthy': True
    },
    'Apple___Apple_scab': {
        'name_en': 'Apple - Apple Scab',
        'name_ta': 'ஆப்பிள் - சொறி நோய்',
        'advice_en': 'Rake and destroy fallen leaves in autumn to prevent overwintering. Apply fungicides during bud burst and early leaf development.',
        'advice_ta': 'நோய் தங்குவதைத் தடுக்க இலையுதிர்காலத்தில் விழுந்த இலைகளைச் சேகரித்து அழிக்கவும். மொட்டு வெடிக்கும் போதும் ஆரம்ப இலை வளர்ச்சியின் போதும் பூஞ்சைக் கொல்லிகளைப் பயன்படுத்தவும்.',
        'is_healthy': False
    },
    'Apple___Black_rot': {
        'name_en': 'Apple - Black Rot',
        'name_ta': 'ஆப்பிள் - கருப்பு அழுகல் நோய்',
        'advice_en': 'Prune out dead wood, cankers, and mummified fruit from the tree. Apply appropriate fungicides. Keep trees well pruned to optimize airflow.',
        'advice_ta': 'மரத்திலிருந்து காய்ந்த மரத்துண்டுகள் மற்றும் அழுகிய பழங்களை கவாத்து செய்து அகற்றவும். பொருத்தமான பூஞ்சைக் கொல்லிகளைப் பயன்படுத்தவும். காற்று ஓட்டத்தை மேம்படுத்த மரங்களை நன்றாக கவாத்து செய்து வைக்கவும்.',
        'is_healthy': False
    },
    'Apple___Cedar_apple_rust': {
        'name_en': 'Apple - Cedar Apple Rust',
        'name_ta': 'ஆப்பிள் - சீடார் துரு நோய்',
        'advice_en': 'Remove nearby cedar/juniper trees if possible as they are alternate hosts. Spray fungicides early in the season when apple buds begin to break.',
        'advice_ta': 'மாற்று விருந்தோம்பியாக இருப்பதால் அருகிலுள்ள சீடார் மரங்களை முடிந்தால் அகற்றவும். ஆப்பிள் மொட்டுகள் உடையத் தொடங்கும் போது பருவத்தின் ஆரம்பத்தில் பூஞ்சைக் கொல்லிகளைத் தெளிக்கவும்.',
        'is_healthy': False
    },
    'Apple___healthy': {
        'name_en': 'Apple - Healthy Leaf',
        'name_ta': 'ஆப்பிள் - ஆரோக்கியமான இலை',
        'advice_en': 'The apple leaf is healthy. Ensure annual pruning is done and monitor fruit quality regularly.',
        'advice_ta': 'ஆப்பிள் இலை ஆரோக்கியமாக உள்ளது. வருடாந்திர கவாத்து செய்யப்படுவதை உறுதிசெய்து, பழங்களின் தரத்தை தவறாமல் கண்காணிக்கவும்.',
        'is_healthy': True
    }
}
# Helper to look up disease metadata. Returns default if class not found.
def get_disease_details(disease_class):
    return DISEASE_DATA.get(disease_class, {
        'name_en': 'Unknown Plant Disease',
        'name_ta': 'அறியப்படாத தாவர நோய்',
        'advice_en': 'Analyze further or consult an agricultural expert. Maintain clean garden tools and quarantine infected plants.',
        'advice_ta': 'மேலும் பகுப்பாய்வு செய்யவும் அல்லது வேளாண்மை நிபுணரை அணுகவும். தோட்டக் கருவிகளை சுத்தமாக வைத்திருங்கள் மற்றும் பாதிக்கப்பட்ட தாவரங்களை தனிமைப்படுத்துங்கள்.',
        'is_healthy': False
    })