import axios from "axios";

const API_BASE_URL = "http://localhost:8000"; // FastAPI backend

export async function fetchTasks() {
  try {
    const response = await axios.get(`${API_BASE_URL}/tasks`);
    return response.data;
  } catch (err) {
    console.error("Failed to fetch tasks", err);
    // Fallback: return an empty task list so UI still renders
    return { tasks: [] };
  }
}
