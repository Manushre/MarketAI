def generate_report(result):

    report = ""

    report += "========================================\n"
    report += "       W01 MARKETING ANALYSIS REPORT\n"
    report += "========================================\n\n"

    report += "CLIENT\n"
    report += "----------------------------------------\n"
    report += result["client"] + "\n\n"

    report += "INDUSTRY\n"
    report += "----------------------------------------\n"
    report += result["industry"] + "\n\n"

    report += "IDEAL CUSTOMER PROFILE (ICP)\n"
    report += "----------------------------------------\n"

    for key, value in result["ICP"].items():
        report += f"{key}: {value}\n"

    report += "\nUNIQUE SELLING PROPOSITION (USP)\n"
    report += "----------------------------------------\n"
    report += result["USP"] + "\n\n"

    report += "MARKETING RECOMMENDATION\n"
    report += "----------------------------------------\n"
    report += result["Recommendation"] + "\n\n"

    report += "AWARENESS STAGES\n"
    report += "----------------------------------------\n"

    for stage, description in result["Awareness Stages"].items():
        report += f"{stage}: {description}\n"

    report += "\nCUSTOMER JOURNEY\n"
    report += "----------------------------------------\n"

    for stage, description in result["Customer Journey"].items():
        report += f"{stage}: {description}\n"

    report += "\nMARKETING FUNNEL\n"
    report += "----------------------------------------\n"

    for stage, description in result["Marketing Funnel"].items():
        report += f"{stage}: {description}\n"

    report += "\nAGENT SUMMARY\n"
    report += "----------------------------------------\n"
    report += result["Agent Summary"] + "\n"

    return report