import { CampLeaderModel } from "./camp-leader-model";

export interface AboutCampModel{
  camp_name: string;
  description: string;
  camp_image: string;
  camp_leader: CampLeaderModel;
}
