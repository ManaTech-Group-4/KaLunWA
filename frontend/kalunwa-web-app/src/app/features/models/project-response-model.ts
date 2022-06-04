export interface ProjectResponseModel{
  id: number;
  title: string;
  description: string;
  image: {
      id: number;
      name: string;
      image: string;
      tags: string[];
      created_at: string;
      updated_at: string;
  },
  start_date: string;
  end_date: string;
  camp: string;
  status: string;
  created_at: SVGStringList;
  updated_at: string;
}
