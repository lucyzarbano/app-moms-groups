export type User = {
  id: number;
  email: string;
  fullName?: string;
  role: string;
};

export type Event = {
  id: number;
  title: string;
  description?: string;
  location?: string;
  startsAt: string;
};

export type Announcement = {
  id: number;
  title: string;
  body: string;
  priority: 'normal' | 'important';
};

export type ChatMessage = {
  id: number;
  chatGroupId: number;
  userId: number;
  body: string;
  createdAt: string;
};
