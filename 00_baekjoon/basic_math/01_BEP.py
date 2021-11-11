#1712 손익분기점
FixedCost, VariableCost, UnitCost = map(int, input().split())

if VariableCost >= UnitCost:
    print(-1)
else:
    print(int(FixedCost/(UnitCost-VariableCost)+1))