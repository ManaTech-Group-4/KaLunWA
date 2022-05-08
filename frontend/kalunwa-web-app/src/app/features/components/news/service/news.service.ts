import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { NewsResponseModel } from 'src/app/features/models/news-model';

@Injectable({
  providedIn: 'root'
})
export class NewsService {

  constructor(private http: HttpClient) {}

  public getNewsList() : Observable<NewsResponseModel[]>{
    return this.http.get<NewsResponseModel[]>('http://127.0.0.1:8000/api/news/?expand=image&omit=created_at,updated_at');
  }
}
