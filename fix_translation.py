import re

with open('c:/Users/Admin/Claude/Projects/IVP Website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    'IVP TISSUE CULTURE CENTER – NEW MILESTONE WITH THE CIRCULATION ANNOUNCEMENT OF KIM CUONG PINEAPPLE': 'IVP TISSUE CULTURE CENTER – NEW MILESTONE WITH THE OFFICIAL RELEASE OF THE KIM CUONG PINEAPPLE VARIETY',
    
    'May 19, 2026 marks a notable milestone in the research and development of plant varieties by IVP Seedlings and Medicinal Plants JSC. The Kim Cuong pineapple variety, selected and propagated by IVP using plant tissue culture methods, has been recorded on the administrative procedure information system of the <a href=\'https://motcua.mae.gov.vn/Pages/TuCongBo.aspx\' target=\'_blank\' rel=\'noopener noreferrer\' style=\'color:var(--primary); font-weight:bold; text-decoration:underline;\'>Ministry of Agriculture and Environment under the form of self-declaration for circulation of plant varieties</a>.': 'May 19, 2026, marks a notable milestone in the research and development of plant varieties by IVP Seedlings and Medicinal Plants JSC. The Kim Cuong pineapple variety, selected and propagated by IVP using plant tissue culture techniques, has been officially recorded on the administrative procedure information system of the <a href=\'https://motcua.mae.gov.vn/Pages/TuCongBo.aspx\' target=\'_blank\' rel=\'noopener noreferrer\' style=\'color:var(--primary); font-weight:bold; text-decoration:underline;\'>Ministry of Agriculture under the form of self-declaration for plant variety circulation</a>.',
    
    'Kim Cuong Pineapple – Shallow eyes, golden flesh, delicious, smooth, fiberless': 'Kim Cuong Pineapple – Shallow eyes, golden flesh, delicious, smooth, and fiberless',
    
    'The Kim Cuong pineapple originated from Taiwan, successfully researched and propagated by IVP using plant tissue culture methods. This technology helps multiply new varieties rapidly for production. IVP strives to research cultivation techniques for Kim Cuong Pineapple suitable for local climate and soil conditions.': 'Originating from Taiwan, the Kim Cuong pineapple has been successfully researched and propagated by IVP using plant tissue culture techniques. This technology enables the rapid multiplication of new varieties for commercial production. IVP is dedicated to researching cultivation protocols for the Kim Cuong pineapple that are tailored to local climate and soil conditions.',
    
    'Some information about the Kim Cuong Pineapple variety': 'Key characteristics of the Kim Cuong Pineapple variety',
    
    '👉 <strong>Growth:</strong> Vigorous growth, spineless leaf margins, yellow-green color, turning pink-red under extreme weather. Leaf length 90-100 cm.': '👉 <strong>Growth habits:</strong> Vigorous growth, spineless leaf margins, and yellow-green foliage that develops a pinkish-red hue under extreme weather conditions. Leaf length is 90-100 cm.',
    
    '👉 <strong>Growth period:</strong> 17 months from planting to harvest completion.': '👉 <strong>Growth cycle:</strong> 17 months from planting to the end of harvest.',
    
    '👉 <strong>Yield:</strong> High yield potential, up to 74 tons/ha under suitable farming conditions.': '👉 <strong>Yield:</strong> High yield potential, capable of reaching 74 tons/ha under optimal farming conditions.',
    
    '👉 <strong>Fruit quality:</strong> Elongated conical or oval shape, hard shell, shallow eyes, distinct aroma. Shell turns from green to golden, orange and brown when ripe. Flesh is deep yellow or golden, smooth, fiberless. Average weight 1.4 kg/fruit. Brix level 16.3%, low acidity.': '👉 <strong>Fruit characteristics & quality:</strong> Elongated conical or oval shape with a hard shell, shallow eyes, and a distinctive aroma. The skin transitions from green to golden, orange, and brown as it ripens. The flesh is deep yellow or golden, smooth, and fiberless. The average fruit weight is 1.4 kg. Brix level reaches 16.3% with low acidity.',
    
    'The circulation announcement of Kim Cuong pineapple is a crucial milestone, showing IVP\'s direction in researching, selecting, breeding and putting high-value crops into production.': 'The official release of the Kim Cuong pineapple variety is a crucial milestone, reflecting IVP\'s strategic direction in researching, breeding, propagating, and introducing high-value crop varieties into commercial production.',
    
    'With the direction from Research - Propagation - Planting - Product Development, IVP focuses not only on seedlings but also on commercial pineapple production projects. The goal is to develop high-quality fresh pineapple products with the best value for domestic consumers. IVP wants everyone to easily enjoy this delicious fruit.': 'Following the integrated model of Research – Propagation – Cultivation – Product Development, IVP focuses not only on producing high-quality seedlings but also on integrating the Kim Cuong pineapple into the company\'s commercial fruit production projects. The ultimate goal is to develop premium fresh pineapples offering the best value to domestic consumers, making this delicious fruit widely accessible.',
    
    'This also reflects IVP\'s commitment to linking Research with practical Production, bringing tissue culture technology from the lab to production zones and ultimately to consumers.': 'This direction also demonstrates IVP\'s commitment to bridging Research with practical Production—translating tissue culture innovations from the laboratory to agricultural fields, and ultimately to the consumer.',
    
    'See details of the self-declaration for circulation of plant varieties in the attached document below:': 'View the detailed Self-Declaration for Plant Variety Circulation in the attached document below:'
}

for old_text, new_text in replacements.items():
    html = html.replace(old_text, new_text)

with open('c:/Users/Admin/Claude/Projects/IVP Website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Translations updated!")
