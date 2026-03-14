import React, { useState } from "react";
import UploadForm from "../components/uploadForm";
import AuditTable from "../components/AuditTable";

function Dashboard() {

  const [audit, setAudit] = useState(null);

  return (
    <div style={{ padding: "40px" }}>

      <h1>Hospital MRD Compliance Audit</h1>

      <UploadForm setAudit={setAudit} />

      <br />

      <AuditTable data={audit} />

    </div>
  );
}

export default Dashboard;