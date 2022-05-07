import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IndivNewsComponent } from './indiv-news.component';

describe('IndivNewsComponent', () => {
  let component: IndivNewsComponent;
  let fixture: ComponentFixture<IndivNewsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IndivNewsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IndivNewsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
