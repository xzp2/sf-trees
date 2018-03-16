import csv

topTrees = {
	"Platanus x hispanica :: Sycamore: London Plane" : "#4CAF50",
	"Metrosideros excelsa :: New Zealand Xmas Tree" : "#f44336",
	"Lophostemon confertus :: Brisbane Box" : "#2196F3",
	"Pittosporum undulatum :: Victorian Box" : "#E91E63",
	"Tristaniopsis laurina :: Swamp Myrtle" : "#FFC107",
	"Prunus cerasifera :: Cherry Plum" : "#FFEB3B",
	"Magnolia grandiflora :: Southern Magnolia" : "#607D8B",
	"Ficus microcarpa nitida 'Green Gem' :: Indian Laurel Fig Tree 'Green Gem'" : "#00BCD4",
	"Arbutus 'Marina' :: Hybrid Strawberry Tree" : "#1976D2",
	"Prunus serrulata 'Kwanzan' :: Kwanzan Flowering Cherry" : "#673AB7",
	"Acacia melanoxylon :: Blackwood Acacia" : "#7B1FA2",
	"Maytenus boaria :: Mayten" : "#00796B",
	"Olea europaea :: Olive Tree" : "#303F9F",
	"Corymbia ficifolia :: Red Flowering Gum" : "#FF9800",
	"Callistemon citrinus :: Lemon Bottlebrush" : "#795548",
	"Ginkgo biloba :: Maidenhair Tree" : "#AFB42B",
	"Pyrus calleryana :: Ornamental Pear" : "#FBC02D",
	"Prunus serrulata :: Ornamental Cherry" : "#9C27B0",
	"Ulmus parvifolia :: Chinese Elm" : "#d32f2f",
	"Eriobotrya deflexa :: Bronze Loquat" : "#388E3C",
	"Ligustrum lucidum :: Glossy Privet" : "#E64A19",
	# "Pinus radiata :: Monterey Pine" : "#A5D6A7",
	# "Pyrus kawakamii :: Evergreen Pear" : "#90CAF9",
	# "Cupressus macrocarpa :: Monterey Cypress" : "#ef9a9a",
	# "Pittosporum crassifolium :: Karo Tree" : "#FFE082",
	# "Tristaniopsis laurina 'Elegant' :: Small-leaf Tristania 'Elegant'" : "#C5E1A5",
	# "Melaleuca quinquenervia :: Cajeput" : "#F48FB1",
	# "Myoporum laetum :: Myoporum" : "#FFCC80",
	# "Cordyline australis :: Dracena Palm" : "#80CBC4",
	# "Ficus nitida :: Laurel Fig" : "#CE93D8",
	# "Liquidambar styraciflua :: American Sweet Gum" : "#81D4FA",
	# "Ficus retusa nitida :: Banyan Fig" : "#B0BEC5",
	# "Juniperus chinensis :: Juniper" : "#BCAAA4",
	# "Tristania conferta ::" : "#EEEEEE",
	# "Jacaranda mimosifolia :: Jacaranda" : "#C5CAE9",
	# "Schinus terebinthifolius :: Brazilian Pepper" : "#E6EE9C",
	# "Eucalyptus polyanthemos :: Silver Dollar Eucalyptus" : "#FFAB91",
	# "Lagunaria patersonii :: Primrose Tree" : "#80DEEA",
	# "Washingtonia robusta :: Mexican Fan Palm" : "#9FA8DA",
	# "Ficus microcarpa :: Chinese Banyan" : "#B39DDB",
	# "Callistemon viminalis :: Weeping Bottlebrush" : "#A1887F",
	# "Agonis flexuosa :: Peppermint Willow" : "#FFF176",
	# "Ceratonia siliqua :: Carob" : "#",
	# "Syagrus romanzoffianum :: Queen Palm" : "#",
	# "Magnolia grandiflora 'Little Gem' :: Little Gem Magnolia" : "#",
	# "Acacia baileyana :: Bailey's Acacia" : "#",
	# "Laurus nobilis :: Sweet Bay: Grecian Laurel" : "#",
	# "Acer rubrum :: Red Maple" : "#",
	# "Rhaphiolepis Majestic Beauty :: Indian Hawthorn  'Majestic Beau'" : "#",
	# "Eucalyptus sideroxylon :: Red Ironbark" : "#",
}

distinctTrees = {}
speciesCount = {}

speciesListFile = open('SpeciesList.csv', 'w')
treesTrimmedFile = open('TreesTrimmed.csv', 'w')

speciesListFile.write("Species,Color\n")

for key in topTrees:
	speciesListFile.write(key.replace("'","") +',' + topTrees[key].replace("'","") + '\n')


with open('Street_Tree_List.csv', 'rb') as csvfile:
	input = csv.reader(csvfile, delimiter=',')
	for row in input:
		if row[2] not in speciesCount:
			speciesCount[row[2]] = 0
		speciesCount[row[2]] += 1

		if row[2] in topTrees or row[2] == "qSpecies":
			outString = row[2] + ',' + row[15] + ',' + row[16] + '\n'
			if outString not in distinctTrees:
				treesTrimmedFile.write(outString.replace("'", ""))
			distinctTrees[outString] = 0

