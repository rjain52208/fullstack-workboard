import React from "react";
import { fetchTasks } from "../api/tasks";

const COLUMN_TITLES = {
  todo: "Todo",
  in_progress: "In Progress",
  done: "Done",
};

export function BoardPage() {
  const [tasks, setTasks] = React.useState([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    // In a real app this would call the backend
    fetchTasks()
      .then((data) => {
        setTasks(data.tasks || []);
      })
      .finally(() => setLoading(false));
  }, []);

  const grouped = {
    todo: [],
    in_progress: [],
    done: [],
  };

  for (const task of tasks) {
    const key = task.status || "todo";
    if (!grouped[key]) grouped[key] = [];
    grouped[key].push(task);
  }

  if (loading) {
    return <div>Loading tasks…</div>;
  }

  return (
    <div style={{ display: "flex", gap: "1rem" }}>
      {Object.entries(COLUMN_TITLES).map(([status, title]) => (
        <div
          key={status}
          style={{
            flex: 1,
            background: "#f7f7f7",
            borderRadius: "8px",
            padding: "0.75rem",
          }}
        >
          <h2 style={{ fontSize: "1.1rem" }}>{title}</h2>
          <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
            {grouped[status].map((task) => (
              <div
                key={task.id}
                style={{
                  background: "white",
                  borderRadius: "6px",
                  padding: "0.5rem 0.75rem",
                  boxShadow: "0 1px 3px rgba(0,0,0,0.08)",
                }}
              >
                <strong>{task.title}</strong>
                {task.description && (
                  <p style={{ margin: "0.25rem 0 0", fontSize: "0.85rem", color: "#555" }}>
                    {task.description}
                  </p>
                )}
              </div>
            ))}
            {grouped[status].length === 0 && (
              <p style={{ fontSize: "0.8rem", color: "#777" }}>No tasks yet.</p>
            )}
          </div>
        </div>
      ))}
    </div>
  );
}
