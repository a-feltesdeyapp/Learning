part def Oven;
part def Building;

part testOven: Oven{
    ref building: Building; // ref is technically an optional keyword but just include it for clarity
}