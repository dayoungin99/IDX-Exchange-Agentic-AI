import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import type { ListingRow } from "./active_listings";

interface UserSession {
  city?: string;
  maxPrice?: number;
  beds?: number;
  baths?: number;
  type?: string;
  pool?: string;
  lastResults?: ListingRow[];
  conversationStep: number;
}

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SESSION_FILE = path.join(__dirname, "../sessions.json");

function loadSessions(): Record<string, UserSession> {
  if (!fs.existsSync(SESSION_FILE)) {
    return {};
  }

  return JSON.parse(fs.readFileSync(SESSION_FILE, "utf-8"));
}

function saveSessions(sessions: Record<string, UserSession>) {
  fs.writeFileSync(
    SESSION_FILE,
    JSON.stringify(sessions, null, 2)
  );
}

export function getSession(userId: string): UserSession {
  const sessions = loadSessions();

  if (!sessions[userId]) {
    sessions[userId] = { conversationStep: 0 };
    saveSessions(sessions);
  }

  return sessions[userId];
}

export function updateSession(
  userId: string,
  updates: Partial<UserSession>
) {
  const sessions = loadSessions();

  sessions[userId] = {
    ...getSession(userId),
    ...updates
  };

  saveSessions(sessions);
}

export function clearSession(userId: string) {
  const sessions = loadSessions();
  delete sessions[userId];
  saveSessions(sessions);
}