import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { NewsResponseModel } from 'src/app/features/models/news-model';

@Component({
  selector: 'app-news-list',
  templateUrl: './news-list.component.html',
  styleUrls: ['./news-list.component.scss']
})
export class NewsListComponent implements OnInit {

  @Input() news = [] as NewsResponseModel[];
  @Input() getLatest: (id: number) => void;
  @Input() latestNews$: Observable<string[]>;

  constructor() { }

  ngOnInit(): void {
  }

}
