from flask import Flask

app = Flask(__name__)

@app.route("/")
def dashboard():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevSecOps Security Dashboard</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #e5e7eb;
            }

            .container {
                padding: 40px;
            }

            .header {
                background: linear-gradient(135deg, #2563eb, #7c3aed);
                padding: 30px;
                border-radius: 16px;
                margin-bottom: 30px;
            }

            .header h1 {
                margin: 0;
                font-size: 36px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
                margin-bottom: 30px;
            }

            .card {
                background: #1e293b;
                padding: 25px;
                border-radius: 16px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            }

            .card h2 {
                margin-top: 0;
                font-size: 22px;
            }

            .passed {
                color: #22c55e;
                font-size: 28px;
                font-weight: bold;
            }

            .score {
                font-size: 50px;
                font-weight: bold;
                color: #38bdf8;
            }

            .status {
                display: inline-block;
                padding: 10px 18px;
                background: #14532d;
                color: #86efac;
                border-radius: 30px;
                font-weight: bold;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                background: #1e293b;
                border-radius: 16px;
                overflow: hidden;
            }

            th, td {
                padding: 16px;
                text-align: left;
                border-bottom: 1px solid #334155;
            }

            th {
                background: #334155;
            }

            .footer {
                margin-top: 30px;
                color: #94a3b8;
                text-align: center;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <div class="header">
                <h1>DevSecOps Security Dashboard</h1>
                <p>Automated security monitoring for CI/CD pipeline</p>
            </div>

            <div class="cards">
                <div class="card">
                    <h2>Pipeline Status</h2>
                    <span class="status">SECURE</span>
                </div>

                <div class="card">
                    <h2>Security Score</h2>
                    <div class="score">100%</div>
                </div>

                <div class="card">
                    <h2>Total Tools</h2>
                    <div class="score">3</div>
                </div>
            </div>

            <table>
                <tr>
                    <th>Security Tool</th>
                    <th>Purpose</th>
                    <th>Status</th>
                </tr>
                <tr>
                    <td>Semgrep</td>
                    <td>SAST Code Security Scanning</td>
                    <td class="passed">Passed</td>
                </tr>
                <tr>
                    <td>Gitleaks</td>
                    <td>Secret Detection</td>
                    <td class="passed">Passed</td>
                </tr>
                <tr>
                    <td>Trivy</td>
                    <td>Docker Image Vulnerability Scanning</td>
                    <td class="passed">Passed</td>
                </tr>
            </table>

            <div class="footer">
                DevSecOps Security Dashboard | Flask + Docker + GitHub Actions
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)