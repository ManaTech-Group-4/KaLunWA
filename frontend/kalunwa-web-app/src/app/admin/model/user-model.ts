export class Admin {
  user_id: number;
  email: string;
  password: string;
  first_name: string;
  last_name: string;
  is_superadmin: boolean;
  image: string;
  exp: number;
}

export class Profile {
  id: number;
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
  is_superadmin: boolean;
  image: string;
}

