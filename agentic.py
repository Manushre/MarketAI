from search_tool import search_web


def marketing_agent(client_name):

    client_data = {
        "Audit 360": {
            "industry": "Audit and compliance",
            "product": "Audit management software",
            "target_customer": "Businesses that manage audits and compliance",
            "problem": "Manual audit processes and difficulty tracking compliance"
        },

        "iTriangle": {
            "industry": "Fleet management and IoT",
            "product": "Fleet tracking and management solutions",
            "target_customer": "Businesses with vehicles and logistics operations",
            "problem": "Difficulty tracking vehicles, drivers and fleet operations"
        }
    }

    # Clean user input
    client_name = client_name.strip()

    # Accept different capitalizations
    if client_name.lower() == "audit 360":
        client_name = "Audit 360"

    elif client_name.lower() == "itriangle":
        client_name = "iTriangle"

    else:
        return {
            "error": "Client not available in agent knowledge base."
        }

    # =======================================
    # STEP 15 - AGENT USES WEB SEARCH TOOL
    # =======================================

    search_result = search_web(
        client_name + " company products services"
    )

    print("\n================================")
    print("WEB RESEARCH")
    print("================================")

    print("Search Query:", search_result["query"])
    print("Search URL:", search_result["search_url"])

    data = client_data[client_name]

    # =======================================
    # STEP 16 - AGENT DECISION LOG
    # =======================================

    print("\n================================")
    print("AGENT DECISION LOG")
    print("================================")

    print("1. Client identified:", client_name)
    print("2. Client data loaded")
    print("3. Web search tool called")
    print("4. ICP generation started")

    # Decide decision maker
    if "audit" in data["industry"].lower():

        decision_maker = (
            "Compliance Manager / Audit Manager / Business Head"
        )

    elif "fleet" in data["industry"].lower():

        decision_maker = (
            "Fleet Manager / Operations Manager / Business Owner"
        )

    else:

        decision_maker = "Business Owner / Department Head"

    print("5. Decision maker identified:", decision_maker)

    # Build ICP
    icp = {
        "Industry": data["industry"],
        "Target Customer": data["target_customer"],
        "Main Problem": data["problem"],
        "Decision Maker": decision_maker,
        "Business Need": data["product"]
    }

    print("6. ICP generated")

    # Create USP
    usp = (
        f"{client_name} helps {data['target_customer']} "
        f"solve {data['problem']} through {data['product']}."
    )

    print("7. USP generated")

    # Marketing recommendation
    if "audit" in data["industry"].lower():

        recommendation = (
            "Focus marketing on compliance leaders, audit managers "
            "and businesses preparing for audits."
        )

    elif "fleet" in data["industry"].lower():

        recommendation = (
            "Focus marketing on fleet managers, logistics companies "
            "and businesses that operate multiple vehicles."
        )

    else:

        recommendation = (
            "Focus marketing on business decision makers."
        )

    print("8. Marketing recommendation generated")

    # =======================================
    # W01 AWARENESS STAGES
    # =======================================

    awareness_stages = {
        "Unaware":
            "Customer does not yet recognize the business problem.",

        "Problem Aware":
            f"Customer understands the problem: {data['problem']}.",

        "Solution Aware":
            f"Customer starts looking for solutions such as {data['product']}.",

        "Product Aware":
            f"Customer evaluates {client_name} and competing solutions.",

        "Most Aware":
            f"Customer is ready to contact {client_name}, request a demo or make a purchase."
    }

    print("9. Awareness stages generated")

    # =======================================
    # W01 CUSTOMER JOURNEY
    # =======================================

    customer_journey = {
        "Awareness":
            "Customer becomes aware of the business problem.",

        "Consideration":
            f"Customer researches solutions related to {data['product']}.",

        "Evaluation":
            f"Customer compares {client_name} with competitors.",

        "Decision":
            f"Customer contacts {client_name} or requests a demo.",

        "Retention":
            "Customer continues using the solution and may recommend it to others."
    }

    print("10. Customer journey generated")

    # =======================================
    # STEP 17 - W01 MARKETING FUNNEL
    # =======================================

    marketing_funnel = {
        "TOFU - Awareness":
            "Use educational blogs, social media content and problem-focused content.",

        "MOFU - Consideration":
            f"Use case studies, product information and comparison content about {data['product']}.",

        "BOFU - Decision":
            f"Use demos, consultations, testimonials and strong calls-to-action to convert customers for {client_name}."
    }

    print("11. Marketing funnel generated")

    # =======================================
    # STEP 18 - AGENT FINAL SUMMARY
    # =======================================

    agent_summary = (
        f"The marketing agent analyzed {client_name}. "
        f"The target customer is {data['target_customer']}. "
        f"The main business problem is {data['problem']}. "
        f"The recommended decision maker is {decision_maker}. "
        f"The agent generated an ICP, USP, awareness stages, "
        f"customer journey and marketing funnel."
    )

    print("12. Final agent summary generated")

    # =======================================
    # FINAL AGENT OUTPUT
    # =======================================

    return {
        "client": client_name,
        "industry": data["industry"],
        "ICP": icp,
        "USP": usp,
        "Recommendation": recommendation,
        "Awareness Stages": awareness_stages,
        "Customer Journey": customer_journey,
        "Marketing Funnel": marketing_funnel,
        "Agent Summary": agent_summary,
        "Search Result": search_result
    }