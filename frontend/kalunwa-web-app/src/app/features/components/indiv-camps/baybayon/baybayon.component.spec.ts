import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BaybayonComponent } from './baybayon.component';

describe('BaybayonComponent', () => {
  let component: BaybayonComponent;
  let fixture: ComponentFixture<BaybayonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BaybayonComponent ],
      imports: [HttpClientTestingModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BaybayonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
