## Tehtävä 3 sekvenssikaavio
```mermaid
sequenceDiagram
    main->>+Machine: Machine()
    Machine->>FuelTank: FuelTank()
    Machine->>+FuelTank: fill(40)
    FuelTank-->>-Machine: 
    Machine->>Engine: Engine(tank)
    main->>Machine: drive()
    Machine->>+Engine: start()
    Engine->>FuelTank: consume(5)
    Engine-->>-Machine: 
    Machine->>Engine: isrunning()
    Engine-->>Machine: True
    Machine->>+Engine: use_energy()
    Engine->>FuelTank: consume(10)
    Engine-->>-Machine: 
```
## Tehtävä 4 sekvenssikaavio
