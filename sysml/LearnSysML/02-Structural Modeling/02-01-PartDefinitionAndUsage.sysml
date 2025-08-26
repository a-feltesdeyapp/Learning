// part: modular unit of structure. system, system component, external entity, etc.
	// hierarchy to allow for different levels of abstraction
	// parts can be logical abstractions, such as orgs, or users
	// connect to product reqs
// definition > usage - typical method of SysML

// Define Part: TitleCase, square corners
	//part def <shortname> Name
		//Shortname is optional, often used as human readable id or to shorten long part names.
part def <P001> Oven;

// Usage: camelCase, rounded corners
	// part usageName: PartName;
		// testOven is usage of part def Oven
part testOven: Oven;
	// part usageName defined by PartName;
part testOven2 defined by Oven;
	// part usageName defined by shortname; or part usageName: shortname
part testOven3: P001;

// Arrow with 2 dots indicates definition. Interpreted as usageName defined by PartName
	// Aka, feature typing relationship
	
	
// SysML has a variety of views based on the relationships between components. This is using a general view
	// General view: structural components and relationships
	// Interconnection view: connection between parts so that they can interact with each other
	// Action flow view
	// State transition view
	// Geometery view (not covered in this course)
	// Case view
	// Grid view (not covered in this course)
	// Browser view (not covered in this course)