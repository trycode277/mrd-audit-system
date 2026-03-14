import React from "react";

function AuditResult({ result }) {

  if (!result) return null;

  return (
    <div>

      <h2>Audit Result</h2>

      <p><b>Compliance Score:</b> {result.compliance_score}%</p>
      <p><b>Risk Level:</b> {result.risk_level}</p>

      <pre>
        {JSON.stringify(result.structured_data, null, 2)}
      </pre>

    </div>
  );
}

export default AuditResult;