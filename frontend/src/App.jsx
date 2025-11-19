import React from "react";
import { BoardPage } from "./pages/BoardPage";

export function App() {
  return (
    <div style={{ fontFamily: "system-ui, sans-serif", padding: "1.5rem" }}>
      <header style={{ marginBottom: "1rem" }}>
        <h1>Fullstack Workboard</h1>
        <p style={{ color: "#555" }}>
          Simple task dashboard powered by a FastAPI backend and React frontend.
        </p>
      </header>
      <BoardPage />
    </div>
  );
}
