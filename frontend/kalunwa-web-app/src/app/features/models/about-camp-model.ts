import { CampLeaderModel } from "./camp-leader-model";

export interface AboutCampModel{
  name: string;
  description: string;
  image: {image: string};
  camp_leader: CampLeaderModel;
}
