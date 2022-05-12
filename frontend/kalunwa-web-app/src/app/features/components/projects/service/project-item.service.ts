import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IndivProjectsModel } from 'src/app/features/models/indiv-project-model';
import { ProjectResponseModel } from 'src/app/features/models/project-response-model';

@Injectable({
  providedIn: 'root'
})
export class ProjectItemService {

  constructor(private http:HttpClient) { }

  public getProjectList() : Observable<ProjectResponseModel[]>{
    return this.http.get<ProjectResponseModel[]>('http://127.0.0.1:8000/api/projects/?expand=image');
  }
  getProjectDetails(projectId: string | null) : Observable<IndivProjectsModel>{
    let address  = 'http://127.0.0.1:8000/api/projects/'+projectId+'/?expand=image,contributors.image,gallery&omit=created_at,updated_at&query_limit_gallery=10';
    return this.http.get<IndivProjectsModel>(address);
  }
}
