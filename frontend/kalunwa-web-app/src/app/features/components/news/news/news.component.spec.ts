import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { NewsService } from '../service/news.service';

import { NewsComponent } from './news.component';

describe('NewsComponent', () => {
  let component: NewsComponent;
  let fixture: ComponentFixture<NewsComponent>;
  let testBedService: NewsService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewsComponent ],
      imports : [ HttpClientTestingModule],
      providers: [NewsService]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NewsComponent);
    component = fixture.componentInstance;
    testBedService = TestBed.get(NewsService);
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('Service injected via inject() and TestBed.get() should be the same instance (NewsService)',
    inject([NewsService], (injectService: NewsService) => {
      expect(injectService).toBe(testBedService);
  }));
});
