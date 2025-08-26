// Attribute
	// A set of data values that represent the properties of an element


// Integer and PowerUnit are not native to SysML and must be called from packages in the sysml.library using import
	// private import LibraryPackage::DataTypeFromLibraryPackage
	// specifies namespaces w/in SysML
private import ScalarValues::Integer;	// ScalarValues: std scalar data types (real, integer, bool, string, etc)
private import SI::PowerUnit;	// SI library: measurement units per ISO 80,000 Std

part def Oven {
	attribute rackCount: Integer;
	attribute wattage: PowerUnit;
}

part testOven: Oven;