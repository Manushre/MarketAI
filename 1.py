from agentic import marketing_agent

print("================================")
print("      W01 MARKETING AGENT")
print("================================")

client_name = input("\nEnter client name: ")

result = marketing_agent(client_name)

if "error" in result:

    print("\nError:", result["error"])

else:

    print("\n================================")
    print("CLIENT")
    print("================================")

    print(result["client"])

    print("\n================================")
    print("INDUSTRY")
    print("================================")

    print(result["industry"])

    print("\n================================")
    print("IDEAL CUSTOMER PROFILE (ICP)")
    print("================================")

    for key, value in result["ICP"].items():
        print(f"{key}: {value}")

    print("\n================================")
    print("UNIQUE SELLING PROPOSITION (USP)")
    print("================================")

    print(result["USP"])

    print("\n================================")
    print("MARKETING RECOMMENDATION")
    print("================================")

    print(result["Recommendation"])