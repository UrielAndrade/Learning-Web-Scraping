const express = require("express");
const { exec } = require("child_process");

const app = express();
app.use(express.static("public"));

app.get("/run-python", (req, res) => {
  exec("python3 ./V2.0SuapScaping.py", (error, stdout, stderr) => {
    if (error) {
      console.error(error);
      return res.status(500).send("Erro ao executar o Python");
    }
    res.send(stdout || "Python executado, mas não retornou nada.");
  });
});

app.listen(3000, () => console.log("Servidor rodando em http://localhost:3000"));
