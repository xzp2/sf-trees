import csv

topTrees = {
	"Platanus x hispanica :: Sycamore: London Plane" : "#A5D6A7",
	"Metrosideros excelsa :: New Zealand Xmas Tree" : "#90CAF9",
	"Lophostemon confertus :: Brisbane Box" : "#ef9a9a",
	"Pittosporum undulatum :: Victorian Box" : "#FFE082",
	"Tristaniopsis laurina :: Swamp Myrtle" : "#C5E1A5",
	"Prunus cerasifera :: Cherry Plum" : "#F48FB1",
	"Magnolia grandiflora :: Southern Magnolia" : "#FFCC80",
	"Ficus microcarpa nitida 'Green Gem' :: Indian Laurel Fig Tree 'Green Gem'" : "#80CBC4",
	"Arbutus 'Marina' :: Hybrid Strawberry Tree" : "#CE93D8",
	"Prunus serrulata 'Kwanzan' :: Kwanzan Flowering Cherry" : "#81D4FA",
	"Acacia melanoxylon :: Blackwood Acacia" : "#B0BEC5",
	"Maytenus boaria :: Mayten" : "#BCAAA4",
	"Olea europaea :: Olive Tree" : "#EEEEEE",
	"Corymbia ficifolia :: Red Flowering Gum" : "#C5CAE9",
	"Callistemon citrinus :: Lemon Bottlebrush" : "#E6EE9C",
	"Ginkgo biloba :: Maidenhair Tree" : "#FFAB91",
	"Pyrus calleryana :: Ornamental Pear" : "#80DEEA",
	"Prunus serrulata :: Ornamental Cherry" : "#9FA8DA",
	"Ulmus parvifolia :: Chinese Elm" : "#B39DDB",
	"Eriobotrya deflexa :: Bronze Loquat" : "#A1887F",
	"Ligustrum lucidum :: Glossy Privet" : "#FFF176",
	# "Pinus radiata :: Monterey Pine" : "#",
	# "Pyrus kawakamii :: Evergreen Pear" : "#",
	# "Cupressus macrocarpa :: Monterey Cypress" : "#",
	# "Pittosporum crassifolium :: Karo Tree" : "#",
	# "Tristaniopsis laurina 'Elegant' :: Small-leaf Tristania 'Elegant'" : "#",
	# "Melaleuca quinquenervia :: Cajeput" : "#",
	# "Myoporum laetum :: Myoporum" : "#",
	# "Cordyline australis :: Dracena Palm" : "#",
	# "Ficus nitida :: Laurel Fig" : "#",
	# "Liquidambar styraciflua :: American Sweet Gum" : "#",
	# "Ficus retusa nitida :: Banyan Fig" : "#",
	# "Juniperus chinensis :: Juniper" : "#",
	# "Tristania conferta ::" : "#",
	# "Jacaranda mimosifolia :: Jacaranda" : "#",
	# "Schinus terebinthifolius :: Brazilian Pepper" : "#",
	# "Eucalyptus polyanthemos :: Silver Dollar Eucalyptus" : "#",
	# "Lagunaria patersonii :: Primrose Tree" : "#",
	# "Washingtonia robusta :: Mexican Fan Palm" : "#",
	# "Ficus microcarpa :: Chinese Banyan" : "#",
	# "Callistemon viminalis :: Weeping Bottlebrush" : "#",
	# "Agonis flexuosa :: Peppermint Willow" : "#",
	# "Ceratonia siliqua :: Carob" : "#",
	# "Syagrus romanzoffianum :: Queen Palm" : "#",
	# "Magnolia grandiflora 'Little Gem' :: Little Gem Magnolia" : "#",
	# "Acacia baileyana :: Bailey's Acacia" : "#",
	# "Laurus nobilis :: Sweet Bay: Grecian Laurel" : "#",
	# "Acer rubrum :: Red Maple" : "#",
	# "Rhaphiolepis Majestic Beauty :: Indian Hawthorn  'Majestic Beau'" : "#",
	# "Eucalyptus sideroxylon :: Red Ironbark" : "#",
}


speciesCount = {}

speciesListFile = open('SpeciesList.csv', 'w')
treesTrimmedFile = open('TreesTrimmed.csv', 'w')

speciesListFile.write("qSpecies,qColor\n")

for key in topTrees:
	speciesListFile.write(key +',' + topTrees[key] + '\n')


with open('Street_Tree_List.csv', 'rb') as csvfile:
	input = csv.reader(csvfile, delimiter=',')
	for row in input:
		if row[2] not in speciesCount:
			speciesCount[row[2]] = 0
		speciesCount[row[2]] += 1

		if row[2] in topTrees or row[2] == "qSpecies":
			treesTrimmedFile.write(row[2] + ',' + row[15] + ',' + row[16] + '\n')

