import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ProjectResponseModel } from 'src/app/features/models/project-response-model';

@Injectable({
  providedIn: 'root'
})
export class ProjectItemService {

  constructor(private http:HttpClient) { }

  public getProjectList() : Observable<ProjectResponseModel[]>{
    return this.http.get<ProjectResponseModel[]>('http://127.0.0.1:8000/api/projects');
  }
}
