import axios from "axios";
import type { OptmizeParams, Resume } from "@/types/types";

const api = axios.create({
  baseURL: "http://127.0.0.1:5000/api",
  headers: {
    "Content-Type": "application/json",
  },
});

export const services = {
  optimizeResume: async (params: OptmizeParams): Promise<Resume> => {
    try {
      const response = await api.post<Resume>("optimize-resume", params);
      return response.data;
    } catch (error) {
      console.log(error);
      throw error;
    }
  },
  getInitialData: async (): Promise<Resume> => {
    try {
      const response = await api.get("/resume");
      return response.data;
    } catch (error) {
      console.log(error);
      throw error;
    }
  },
  generatePdf: async (data: Resume): Promise<Blob> => {
    try {
      const response = await api.post("/generate-resume", data, {
        responseType: "blob",
      });
      return response.data;
    } catch (error) {
      console.log(error);
      throw error;
    }
  },
};
