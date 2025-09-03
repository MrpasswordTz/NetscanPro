# New feature: Generate simple report
import os
import datetime
from .module import ensure_reports_dir, REPORTS_DIR, logger, analyze_vulnerabilities

def generate_professional_report(scan_data):
    ensure_reports_dir()
    scan_name = scan_data['name']
    target = scan_data['target']
    timestamp = scan_data['timestamp']
    results = scan_data['results']
    vulnerabilities = analyze_vulnerabilities(results)
    report_file = os.path.join(REPORTS_DIR, f"{scan_name}_report.html")
    with open(report_file, "w") as f:
        f.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NetscanPro V2 Report - {scan_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
        .header {{ background-color: #2c3e50; color: white; padding: 20px; border-radius: 5px; }}
        .section {{ background-color: white; margin: 20px 0; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        .vulnerability {{ background-color: #ffeaa7; border-left: 5px solid #d63031; padding: 10px; margin: 10px 0; }}
        .safe {{ background-color: #55efc4; border-left: 5px solid #00b894; padding: 10px; margin: 10px 0; }}
        pre {{ background-color: #ecf0f1; padding: 10px; border-radius: 3px; overflow-x: auto; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>NetscanPro Security Scan V2 Report</h1>
        <p><strong>Scan Name:</strong> {scan_name}</p>
        <p><strong>Target:</strong> {target}</p>
        <p><strong>Scan Date:</strong> {timestamp}</p>
    </div>

    <div class="section">
        <h2>Scan Results</h2>
        <pre>{results}</pre>
    </div>

    <div class="section">
        <h2>Vulnerability Analysis</h2>
""")

        if vulnerabilities:
            for vuln in vulnerabilities:
                f.write(f"""
        <div class="vulnerability">
            <h3>Port {vuln['port']} - {vuln['service']}</h3>
""")
                for v in vuln['vulnerabilities']:
                    f.write(f"""
            <p><strong>CVE:</strong> {v['cve']}</p>
            <p><strong>Description:</strong> {v['description']}</p>
            <p><strong>Impact:</strong> {v['impact']}</p>
            <p><strong>Recommendation:</strong> {v['fix']}</p>
""")
                f.write("</div>")
        else:
            f.write('<div class="safe"><p>No known vulnerabilities detected in the scan results.</p></div>')

        f.write("""
    </div>

    <div class="section">
        <h2>Recommendations</h2>
        <ul>
            <li>Regularly update all services and operating systems</li>
            <li>Use firewalls to restrict unnecessary port access</li>
            <li>Implement intrusion detection systems</li>
            <li>Conduct regular security audits</li>
        </ul>
    </div>
</body>
</html>
""")

    print(f"Professional report generated: {report_file}")
    logger.info(f"Professional report generated: {report_file}")
