// Multiplicity or Cardinality
// Allowed number of values a usage may have for any instance
	// Single number: fixed value
	// Lower-Upper bounds: natural number
part def Oven;
part def Rack;
	
part oven1: Oven{
	part racks[2]: Rack;	// number of racks is fixed
}

part oven2: Oven{
	part racks[1..3]: Rack;	// number of racks can vary between 1-3 racks
}