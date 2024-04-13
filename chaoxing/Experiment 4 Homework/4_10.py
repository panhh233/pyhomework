for A in range(1, 10):
    for B in range(10):
        for C in range(10):
            for D in range(10):
                if (A * 1000 + B * 100 + C * 10 + D) - (C * 100 + D * 10 + C) == (A * 100 + B * 10 + C):
                    print(f"A={A} B={B} C={C} D={D}")
                    break