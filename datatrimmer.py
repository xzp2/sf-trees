import csv

topTrees = {
<<<<<<< HEAD
	"Platanus x hispanica :: Sycamore: London Plane",
	"Metrosideros excelsa :: New Zealand Xmas Tree",
	"Lophostemon confertus :: Brisbane Box",
	"Pittosporum undulatum :: Victorian Box",
	"Tristaniopsis laurina :: Swamp Myrtle",
	"Prunus cerasifera :: Cherry Plum",
	"Magnolia grandiflora :: Southern Magnolia",
	"Ficus microcarpa nitida 'Green Gem' :: Indian Laurel Fig Tree 'Green Gem'",
	"Arbutus 'Marina' :: Hybrid Strawberry Tree",
	"Prunus serrulata 'Kwanzan' :: Kwanzan Flowering Cherry",
	"Acacia melanoxylon :: Blackwood Acacia",
	"Maytenus boaria :: Mayten",
	"Olea europaea :: Olive Tree",
	"Corymbia ficifolia :: Red Flowering Gum",
	"Callistemon citrinus :: Lemon Bottlebrush",
	"Ginkgo biloba :: Maidenhair Tree",
	"Pyrus calleryana :: Ornamental Pear",
	"Prunus serrulata :: Ornamental Cherry",
	"Ulmus parvifolia :: Chinese Elm",
	"Eriobotrya deflexa :: Bronze Loquat",
	# "Ligustrum lucidum :: Glossy Privet",
	# "Pinus radiata :: Monterey Pine",
	# "Pyrus kawakamii :: Evergreen Pear",
	# "Cupressus macrocarpa :: Monterey Cypress",
	# "Pittosporum crassifolium :: Karo Tree",
	# "Tristaniopsis laurina 'Elegant' :: Small-leaf Tristania 'Elegant'",
	# "Melaleuca quinquenervia :: Cajeput",
	# "Myoporum laetum :: Myoporum",
	# "Cordyline australis :: Dracena Palm",
	# "Ficus nitida :: Laurel Fig",
	# "Liquidambar styraciflua :: American Sweet Gum",
	# "Ficus retusa nitida :: Banyan Fig",
	# "Juniperus chinensis :: Juniper",
	# "Tristania conferta ::",
	# "Jacaranda mimosifolia :: Jacaranda",
	# "Schinus terebinthifolius :: Brazilian Pepper",
	# "Eucalyptus polyanthemos :: Silver Dollar Eucalyptus",
	# "Lagunaria patersonii :: Primrose Tree",
	# "Washingtonia robusta :: Mexican Fan Palm",
	# "Ficus microcarpa :: Chinese Banyan",
	# "Callistemon viminalis :: Weeping Bottlebrush",
	# "Agonis flexuosa :: Peppermint Willow",
	# "Ceratonia siliqua :: Carob",
	# "Syagrus romanzoffianum :: Queen Palm",
	# "Magnolia grandiflora 'Little Gem' :: Little Gem Magnolia",
	# "Acacia baileyana :: Bailey's Acacia",
	# "Laurus nobilis :: Sweet Bay: Grecian Laurel",
	# "Acer rubrum :: Red Maple",
	# "Rhaphiolepis Majestic Beauty :: Indian Hawthorn  'Majestic Beau'",
	# "Eucalyptus sideroxylon :: Red Ironbark",
}


speciesCount = {}

speciesListFile = open('SpeciesList.csv', 'w')
treesTrimmedFile = open('TreesTrimmed.csv', 'w')

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

