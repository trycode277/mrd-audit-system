import React, { useState } from "react";
import axios from "axios";

function UploadForm({ setResult }) {

  const [file, setFile] = useState(null);

  const uploadFile = async () => {

    if (!file) {
      alert("Select file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

const response = await axios.post(
  "http://127.0.0.1:8000/upload",
  formData,
  {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }
);

    setResult(response.data);
  };

  return (
    <div>
      <h3>Upload Medical Record</h3>

      <input type="file" onChange={(e)=>setFile(e.target.files[0])} />

      <button onClick={uploadFile}>
        Upload
      </button>
    </div>
  );
}

export default UploadForm;