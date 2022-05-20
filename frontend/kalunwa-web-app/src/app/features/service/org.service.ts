import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { MembersDialogModel } from '../models/members-dialog-model';

@Injectable({
  providedIn: 'root'
})
export class OrgService {

  constructor(private http: HttpClient) { }

  getExec() : Observable<MembersDialogModel[]>{
    return this.http.get<MembersDialogModel[]>('http://127.0.0.1:8000/api/orgleaders/?expand=image&omit=created_at,updated_at');
  }

  getCampLeaders(camp: string) : Observable<MembersDialogModel[]>{
    let address = "http://127.0.0.1:8000/api/campleaders/?expand=image&omit=created_at,updated_at,camp,motto&camp="+camp;
    return this.http.get<MembersDialogModel[]>(address);
  }

  getGrievance() : Observable<MembersDialogModel[]>{
    return this.http.get<MembersDialogModel[]>('http://127.0.0.1:8000/api/commissioners/?expand=image&omit=created_at,updated_at&category=Grievance%20and%20Ethics');
  }

  getElection() : Observable<MembersDialogModel[]>{
    return this.http.get<MembersDialogModel[]>('http://127.0.0.1:8000/api/commissioners/?expand=image&omit=created_at,updated_at&category=Election');
  }

  getCabin() : Observable<MembersDialogModel[]>{
    return this.http.get<MembersDialogModel[]>('http://127.0.0.1:8000/api/cabinofficers/?expand=image&omit=created_at,updated_at');
  }
}
