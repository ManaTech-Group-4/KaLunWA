import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubaComponent } from './suba.component';

describe('SubaComponent', () => {
  let component: SubaComponent;
  let fixture: ComponentFixture<SubaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SubaComponent ],
      imports: [HttpClientTestingModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SubaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
