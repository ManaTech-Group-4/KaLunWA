import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IndivNewsModel } from 'src/app/features/models/indiv-news-model';
import { NewsResponseModel } from 'src/app/features/models/news-model';

@Injectable({
  providedIn: 'root'
})
export class NewsService {

  constructor(private http: HttpClient) {}

  getNewsList() : Observable<NewsResponseModel[]>{
    return this.http.get<NewsResponseModel[]>('http://127.0.0.1:8000/api/news/?expand=image&omit=created_at,updated_at');
  }

  public getNewsDetails(newsId: string | null) : Observable<IndivNewsModel>{
    let address  = 'http://127.0.0.1:8000/api/news/'+newsId+'/?expand=image&omit=created_at,updated_at';
    return this.http.get<IndivNewsModel>(address);
  }

  public getLatestNews(newsId:string | null): Observable<{id: number, title: string}[]>{
    let address  = 'http://127.0.0.1:8000/api/news/?id__not='+newsId+'&query_limit=3';
    return this.http.get<{id: number, title: string}[]>(address);
  }
}
